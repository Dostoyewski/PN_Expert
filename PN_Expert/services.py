import datetime

from diagnostic.models import Event
from sheduling.models import SurveyShedule


def create_events(pk):
    print("Creating events for object ", pk)
    obj = SurveyShedule.objects.get(pk=pk)
    for user in obj.users.all():
        Event.objects.create(description="Пройти тест " + obj.survey.title,
                             summary="Пройти тест",
                             location="",
                             end=datetime.datetime.now() + datetime.timedelta(days=1),
                             user=user,
                             survey_pk=obj.survey.pk,
                             event_type=4)
