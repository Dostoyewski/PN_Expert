from django.contrib.auth.models import User
from django.db import models

TYPES = (
    (0, "Таблетка"),
    (1, "Капсула"),
    (2, "Спрей"),
    (3, "Мазь"),
    (4, "Пластырь"),
    (5, "Укол"),
)


class Pill(models.Model):
    """
    Класс таблетки (препарата)
    """
    title = models.CharField(max_length=500)
    info = models.TextField(max_length=1000, blank=True)
    # time1 = models.TimeField(default=datetime.time(hour=16, minute=0, second=0))
    # time2 = models.TimeField(blank=True, null=True)
    time = models.TextField(max_length=1000, default="")
    typo = models.IntegerField(choices=TYPES, default=1)

    def __str__(self):
        return self.title


class AssignedPill(models.Model):
    """
    Свзующее звено для таблеток и пользователей. Необходимо для того,
    чтобы таблетки не удалялись при удалении пользователя
    """
    pill = models.ForeignKey(Pill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Дата приема до
    time_out = models.DateField(auto_now_add=True, null=True)
    # Статус, если принимается — то true
    is_taken = models.BooleanField(default=True)
    extra = models.CharField(max_length=500, blank=True, default="")
    dosege = models.CharField(max_length=500, default="")
