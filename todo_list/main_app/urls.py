from django.urls import path
from .views import ProjectListView, ProjectDetailView, TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, \
    TaskDeleteView, CommentCreateView, TaskCompleteView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path("task/<int:pk>/complete/", TaskCompleteView.as_view(), name="task-complete"),


]
