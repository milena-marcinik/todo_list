from django.urls import path, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .models import TasksDay, Task

urlpatterns = [
    path("", ListView.as_view(model='TasksDay'), name='main_todo'),
    path('tasksday/create', CreateView.as_view(model=TasksDay, fields="__all__", success_url=reverse_lazy('main_todo')),
         name='create-tasks-day'),
    path('tasksday/<int:pk>', DetailView.as_view(model=TasksDay), name='taksday-detail'),
    path('task/create', CreateView.as_view(model=Task, fields="__all__", success_url=reverse_lazy('main_todo')),
         name="task-create"),
    path('test', TemplateView.as_view(template_name='todo/base.html'))
]
