from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    re_path(r'^edit/(?P<task_id>\d+)/$', views.task_edit, name='task_edit'),
    re_path(r'^delete/(?P<task_id>\d+)/$', views.task_delete, name='task_delete'),
    re_path(r'^detail/(?P<task_id>\d+)/$', views.task_detail, name='task_detail'),
    re_path(r'^status/(?P<task_id>\d+)/$', views.task_status, name='task_status'),
]
