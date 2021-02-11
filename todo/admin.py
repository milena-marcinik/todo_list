from django.contrib import admin

from todo.models import Task, TasksDay

admin.site.register(Task)
admin.site.register(TasksDay)
