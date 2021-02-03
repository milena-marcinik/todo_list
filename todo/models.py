from django.db import models

# Create your models here.


class TodoItem(models.Model):
    do_name = models.CharField(max_length=200)
    do_date = models.DateTimeField(auto_now_add=True)

