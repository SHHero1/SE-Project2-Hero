from django.urls import path
from . import views
urlpatterns = [
    path('',views.TaskFormView.as_view(),name="store_task"),
    path('task_list/',views.TaskListView.as_view(),name='taskList'),
    path('edit_task/<int:pk>',views.TaskUpdateView.as_view(),name="editTask"),
    path('delete_task/<int:pk>',views.DeleteTaskView.as_view(),name="deleteTask"),
    path('complete_task/<int:pk>',views.CompletedTaskView.as_view(),name="completedTask"),
    path('completed_taskList/',views.CompletedTaskListView.as_view(),name="completedTaskList"),
    path('completed_edit_task/<int:pk>',views.CompletedTaskUpdateView.as_view(),name="completed_editTask"),
    path('completed_delete_task/<int:pk>',views.CompletedDeleteTaskView.as_view(),name="completed_deleteTask"),
]