from django.urls import path
app_name = "todo_list"

from .views import TaskView
urlpatterns = [
    path('task/', TaskView.as_view(), name='task'),
]