import os
from django.shortcuts import render

def explore(request, folder_path=""):
    base_dir = os.getcwd()
    full_path = os.path.join(base_dir, folder_path)

    if not os.path.exists(full_path):
        return render(request, 'file_list.html', {
            'files': [],
            'current_path': folder_path
        })

    items = os.listdir(full_path)

    file_list = []
    for item in items:
        item_path = os.path.join(full_path, item)

        file_list.append({
            'name': item,
            'is_dir': os.path.isdir(item_path),
            'path': os.path.join(folder_path, item).replace("\\", "/")
        })

    return render(request, 'file_list.html', {
        'files': file_list,
        'current_path': folder_path
    })