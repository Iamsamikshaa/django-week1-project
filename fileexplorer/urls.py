from django.contrib import admin
from django.urls import path, re_path
from explorer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('explore/', views.explore, name='explore_root'),
    re_path(r'^explore/(?P<path>.*)/$', views.explore, name='explore'),
]
