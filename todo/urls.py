from django.contrib import admin
from django.urls import path

from todo.views import todo_view, add_todo, delete_todo

urlpatterns = [
    path('', todo_view, name='todo_view'),
    path('add_todo/', add_todo, name='add_todo'),
    path('delete_todo/<int:todo_id>', delete_todo, name='delete_todo'),
    ]
