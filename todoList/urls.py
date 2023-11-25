from django.urls import path
from .views import *

urlpatterns = [
    path('list/', get_tasks_list, name='get_tasks_list'),
    path('list/<int:task_id>/', get_task_details, name='get_task_details'),
    path('list/create/', create_task, name='create_task'),
    path('list/<int:task_id>/update/', update_task, name='update_task'),
    path('list/<int:task_id>/delete/', delete_task, name='delete_task'),
]