import datetime

from django.contrib.auth.models import User
from django.db import models

from diagnostic.models import Event


class Survey(models.Model):
    users = models.ManyToManyField(User)
    points = models.IntegerField(default=0)
    num_q = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        end = datetime.datetime.now()
        end = end.replace(hour=23, minute=59)
        super().save(*args, **kwargs)  # Call the "real" save() method.
        for user in self.users.all():
            Event.objects.create(user=user,
                                 description=self.description,
                                 summary=self.title,
                                 location="—",
                                 end=end,
                                 event_type=4
                                 )


TYPES = (
    (0, "RADIO"),
    (1, "TEXT"),
    (2, "MULTPLY")
)


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.TextField(max_length=100)
    typo = models.IntegerField(choices=TYPES, default=1)
    # Should be separated using ::
    choices = models.CharField(max_length=200, blank=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Should be separated using ',' if Multiply
    answer = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def parse_answers(self):
        if self.question.typo == 2:
            return self.answer.split(sep=',')
        return self.answer
