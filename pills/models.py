import datetime

from django.contrib.auth.models import User
from django.db import models


class Pill(models.Model):
    """
    Класс таблетки (препарата)
    """
    title = models.CharField(max_length=500)
    info = models.TextField(max_length=1000)
    dosege = models.CharField(max_length=500)
    end = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(default=datetime.time(hour=16, minute=0, second=0))
    extra = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class AssignedPill(models.Model):
    """
    Свзующее звено для таблеток и пользователей. Необходимо для того,
    чтобы таблетки не удалялись при удалении пользователя
    """
    pill = models.ForeignKey(Pill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
