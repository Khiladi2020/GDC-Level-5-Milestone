from django.contrib import admin
from django.urls import path

from tasks.views import (
    delete_completed_task_view,
    tasks_view,
    add_task_view,
    delete_task_view,
    delete_completed_task_view,
    mark_complete_task_view,
    completed_tasks_view,
    all_tasks_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Add all your views here
    path("tasks/", tasks_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:task_id>/", delete_task_view),
    path("delete-task/completed/<int:task_id>/", delete_completed_task_view),
    path("complete_task/<int:task_id>/", mark_complete_task_view),
    path("completed_tasks/", completed_tasks_view),
    path("all_tasks/", all_tasks_view),
]
