from django.contrib import admin
from django.urls import path, re_path
from explorer import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.explore),

    path('explore/', views.explore, name='explore_root'),

    re_path(
        r'^explore/(?P<path>.*)/$',
        views.explore,
        name='explore'
    ),

    re_path(
        r'^download/(?P<path>.*)$',
        views.download_file,
        name='download'
    ),

    re_path(
        r'^upload/(?P<path>.*)$',
        views.upload_file,
        name='upload'
    ),

    re_path(
        r'^delete/(?P<path>.*)$',
        views.delete_file,
        name='delete'
    ),

    re_path(
        r'^preview/(?P<path>.*)$',
        views.preview_file,
        name='preview'
    ),

]