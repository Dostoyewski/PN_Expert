import datetime

from django.contrib.auth.models import User
from django.db import models
from django_q.models import Schedule
from django_q.tasks import schedule

from diagnostic.models import Event

SHEDULE_TYPE = (
    (0, 'Ежедневно'),
    (1, 'Раз в неделю'),
    (2, 'Раз в месяц'),
    (3, 'Раз в квартал')
)

TYPES = (
    (0, 'Мероприятие'),
    (1, 'Прием лекарств'),
    (2, 'Видео тест'),
    (3, 'Отправка фотографии'),
    (4, 'Опрос'),
)


class SurveyShedule(models.Model):
    run_interval = models.IntegerField(choices=SHEDULE_TYPE, default=0)
    survey = models.ForeignKey('survey.Survey', on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.run_interval == 0:
            schedule("PN_Expert.services.create_events", self.pk,
                     schedule_type=Schedule.DAILY,
                     next_run=datetime.datetime.now() + datetime.timedelta(seconds=10))
        elif self.run_interval == 1:
            schedule("PN_Expert.services.create_events", self.pk,
                     schedule_type=Schedule.WEEKLY)
        elif self.run_interval == 2:
            schedule("PN_Expert.services.create_events", self.pk,
                     schedule_type=Schedule.MONTHLY)
        elif self.run_interval == 3:
            schedule("PN_Expert.services.create_events", self.pk,
                     schedule_type=Schedule.QUARTERLY)


class MessageSurvey(models.Model):
    run_interval = models.IntegerField(choices=SHEDULE_TYPE, default=0)
    message = models.TextField(default=" ")
    users = models.ManyToManyField(User)
    typo = models.IntegerField(choices=TYPES)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.run_interval == 0:
            schedule("PN_Expert.services.create_events_message", self.pk,
                     schedule_type=Schedule.DAILY,
                     next_run=datetime.datetime.now() + datetime.timedelta(seconds=10))
        elif self.run_interval == 1:
            schedule("PN_Expert.services.create_events_message", self.pk,
                     schedule_type=Schedule.WEEKLY)
        elif self.run_interval == 2:
            schedule("PN_Expert.services.create_events_message", self.pk,
                     schedule_type=Schedule.MONTHLY)
        elif self.run_interval == 3:
            schedule("PN_Expert.services.create_events_message", self.pk,
                     schedule_type=Schedule.QUARTERLY)
