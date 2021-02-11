from django.urls import path, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TasksDay, Task

urlpatterns = [
    path("", ListView.as_view(model=TasksDay), name='main_todo'),
    path('tasksday/create', CreateView.as_view(model=TasksDay, fields="__all__", success_url=reverse_lazy('main_todo')),
         name='tasksday-create'),
    path('tasksday/<int:pk>', DetailView.as_view(model=TasksDay), name='taksday-detail'),
    path('task/create', CreateView.as_view(model=Task, fields="__all__", success_url=reverse_lazy('main_todo')),
         name="task-create"),
    path('test', TemplateView.as_view(template_name='todo/base.html'))
]
