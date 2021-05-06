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


def create_events(users):
    print("asdasd")


class SurveyShedule(models.Model):
    run_interval = models.IntegerField(choices=SHEDULE_TYPE, default=0)
    survey = models.ForeignKey('survey.Survey', on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    # def create_event(self):
    #     # for user in self.users.all():
    #     #     Event.objects.create(description="Пройти тест " + self.survey.title,
    #     #                          summary="Пройти тест",
    #     #                          location="",
    #     #                          end=datetime.datetime.now() + datetime.timedelta(days=1),
    #     #                          user=user,
    #     #                          survey_pk=self.survey.pk,
    #     #                          event_type=4)
    #     print("lkdflsdjf")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        users = self.users.all()
        # if self.run_interval == 0:
        #     schedule(create_events, users,
        #              schedule_type=Schedule.DAILY,
        #              next_run=datetime.datetime.now() + datetime.timedelta(seconds=10))
        # elif self.run_interval == 1:
        #     schedule(create_events, users,
        #              schedule_type=Schedule.WEEKLY)
        # elif self.run_interval == 2:
        #     schedule(create_events, users,
        #              schedule_type=Schedule.MONTHLY)
        # elif self.run_interval == 3:
        #     schedule(create_events, users,
        #              schedule_type=Schedule.QUARTERLY)
        schedule('math.sqrt',
                 9,
                 hook='hooks.print_result',
                 q_options={'timeout': 30, 'broker_name': 'broker_1'},
                 schedule_type=Schedule.HOURLY)
