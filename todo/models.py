from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class TasksDay(models.Model):
    day_date = models.DateField(unique=True)
    owner = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('day_date', 'owner')
        ordering = ('-day_date',)
        verbose_name = "Dzień"
        verbose_name_plural = "Dni"

    def __str__(self):
        return f"{self.day_date}"


class Task(models.Model):
    STATUSES = (('c', 'Czeka'), ('z', 'Zakończony'))
    PRIORITIES = (('w', 'Wysoki'), ('s', 'Średni'), ('n', 'Niski'))

    day = models.ForeignKey(TasksDay, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, verbose_name="Temat")
    description = models.TextField(verbose_name="Opis zadania")
    status = models.CharField(max_length=1, choices=STATUSES, default='c')
    priority = models.CharField(max_length=1, choices=PRIORITIES)
    owner = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    class Meta:
        ordering = ('-day', 'priority')
        verbose_name = 'Zadanie'
        verbose_name_plural = 'Zadania'

    def __str__(self):
        return f"{self.title} {self.day}"

    def clean(self):
        if self.owner != self.day.owner:
            raise ValidationError("Błędny użytkownik")
