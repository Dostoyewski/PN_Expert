import datetime

from django.contrib.auth.models import User

from diagnostic.models import Event
from sheduling.models import SurveyShedule, MessageSurvey


def create_events(pk):
    print("Creating events for object ", pk)
    obj = SurveyShedule.objects.get(pk=pk)
    if not obj.forall:
        for user in obj.users.all():
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
            Event.objects.create(description="Пройти тест " + obj.survey.title,
                                 summary="Пройти тест",
                                 location="",
                                 end=datetime.datetime.now() + datetime.timedelta(days=1),
                                 user=user,
                                 survey_pk=obj.survey.pk,
                                 event_type=4)


def create_events_message(pk):
    print("Creating messages for object ", pk)
    obj = MessageSurvey.objects.get(pk=pk)
    if not obj.forall:
        for user in obj.users.all():
            Event.objects.create(description=obj.message,
                                 summary="Внимание!",
                                 location="",
                                 end=datetime.datetime.now() + datetime.timedelta(days=1),
                                 user=user,
                                 survey_pk=1,
                                 event_type=obj.typo)
    else:
        users = User.objects.all()
        for user in users:
            Event.objects.create(description=obj.message,
                                 summary="Внимание!",
                                 location="",
                                 end=datetime.datetime.now() + datetime.timedelta(days=1),
                                 user=user,
                                 survey_pk=1,
                                 event_type=obj.typo)
