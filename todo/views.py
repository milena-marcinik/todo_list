from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from todo.models import TodoItem

# Create your views here.


def todo_view(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo/base.html', {'all_items': all_todo_items})


def add_todo(request):
    new_item = TodoItem(do_name=request.POST['do_name'], do_date=request.POST['do_date'])
    new_item.save()
    return HttpResponseRedirect(reverse('todo_view'))


def delete_todo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect(reverse('todo_view'))


