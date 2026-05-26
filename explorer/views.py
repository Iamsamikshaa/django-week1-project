import os

from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, FileResponse
from django.conf import settings

from datetime import datetime


BASE_EXPLORER_DIR = os.path.join(
    settings.BASE_DIR,
    "public_files"
)


def explore(request, path=''):

    safe_base = os.path.abspath(BASE_EXPLORER_DIR)

    requested_path = os.path.abspath(
        os.path.join(safe_base, path)
    )

    if not requested_path.startswith(safe_base):
        return HttpResponseForbidden("Access Denied")

    if not os.path.exists(requested_path):

        return render(
            request,
            'explorer/error.html',
            {
                'error': 'Path not found'
            }
        )

    items = []

    try:

        for item in os.listdir(requested_path):

            if item.startswith('.'):
                continue

            full_path = os.path.join(
                requested_path,
                item
            )

            items.append({

                'name': item,

                'is_dir': os.path.isdir(full_path),

                'size': os.path.getsize(full_path),

                'modified': datetime.fromtimestamp(
                    os.path.getmtime(full_path)
                ).strftime('%d-%m-%Y %H:%M'),

                'path': os.path.relpath(
                    full_path,
                    safe_base
                ).replace('\\', '/')

            })

    except Exception as e:

        return render(
            request,
            'explorer/error.html',
            {
                'error': str(e)
            }
        )

    breadcrumbs = []

    temp_path = ''

    if path:

        parts = path.split('/')

        for part in parts:

            temp_path = os.path.join(
                temp_path,
                part
            )

            breadcrumbs.append({

                'name': part,

                'path': temp_path.replace(
                    '\\',
                    '/'
                )

            })

    context = {

        'items': items,

        'current_path': path,

        'breadcrumbs': breadcrumbs,

    }

    return render(
        request,
        'explorer/explore.html',
        context
    )


def download_file(request, path):

    file_path = os.path.join(
        BASE_EXPLORER_DIR,
        path
    )

    return FileResponse(
        open(file_path, 'rb'),
        as_attachment=True
    )


def upload_file(request, path=''):

    if request.method == 'POST':

        uploaded_file = request.FILES.get('file')

        if uploaded_file:

            current_path = os.path.join(
                BASE_EXPLORER_DIR,
                path
            )

            save_path = os.path.join(
                current_path,
                uploaded_file.name
            )

            with open(save_path, 'wb+') as destination:

                for chunk in uploaded_file.chunks():

                    destination.write(chunk)

    return redirect(request.META.get('HTTP_REFERER'))


def delete_file(request, path):

    file_path = os.path.join(
        BASE_EXPLORER_DIR,
        path
    )

    if os.path.isfile(file_path):

        os.remove(file_path)

    return redirect(request.META.get('HTTP_REFERER'))


def preview_file(request, path):

    file_path = os.path.join(
        BASE_EXPLORER_DIR,
        path
    )

    return FileResponse(
        open(file_path, 'rb')
    )