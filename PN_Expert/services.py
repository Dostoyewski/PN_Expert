import datetime
from random import randint
from time import sleep

from django.contrib.auth.models import User

from diagnostic.models import Event
from sheduling.models import SurveyShedule, MessageSurvey


def create_events(pk):
    print("Creating events for object ", pk)
    obj = SurveyShedule.objects.get(pk=pk)
    if not obj.forall:
        for user in obj.users.all():
            sleep(randint(5, 100))
            Event.objects.create(description="Пройти тест " + obj.survey.title,
                                 summary="Пройти тест",
                                 location="",
                                 end=datetime.datetime.now() + datetime.timedelta(days=1),
                                 user=user,
                                 survey_pk=obj.survey.pk,
                                 event_type=4)
    else:
        users = User.objects.all()
        for user in users:
            sleep(randint(5, 100))
            Event.objects.create(description="Пройти тест " + obj.survey.title,
                                 summary="Пройти тест",
                                 location="",
                                 end=datetime.datetime.now() + datetime.timedelta(days=1),
                                 user=user,
                                 survey_pk=obj.survey.pk,
                                 event_type=4)


def construct_string(typo):
    if typo == 0:
        return 'Мероприятие'
    elif typo == 1:
        return 'Прием лекарств'
    elif typo == 2:
        return 'Видео тест'
    elif typo == 3:
        return 'Отправка фотографии'
    elif typo == 4:
        return 'Опрос'


def create_events_message(pk):
    print("Creating messages for object ", pk)
    obj = MessageSurvey.objects.get(pk=pk)
    if not obj.forall:
        for user in obj.users.all():
            sleep(randint(5, 100))
            Event.objects.create(description=obj.message,
                                 summary=construct_string(obj.typo),
                                 location=obj.location,
                                 end=datetime.datetime.now() + datetime.timedelta(days=1),
                                 user=user,
                                 survey_pk=1,
                                 event_type=obj.typo)
    else:
        users = User.objects.all()
        for user in users:
            sleep(randint(5, 100))
            Event.objects.create(description=obj.message,
                                 summary=construct_string(obj.typo),
                                 location=obj.location,
                                 end=datetime.datetime.now() + datetime.timedelta(days=1),
                                 user=user,
                                 survey_pk=1,
                                 event_type=obj.typo)
