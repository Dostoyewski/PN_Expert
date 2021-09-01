import datetime
import os

import pandas as pd
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from PN_Expert.settings import MEDIA_ROOT as media
from diagnostic.models import Event, DataRecording
from lk.models import UserProfile
from .processors import process_test


class Survey(models.Model):
    users = models.ManyToManyField(User)
    points = models.IntegerField(default=0)
    num_q = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.title)


@receiver(m2m_changed, sender=Survey)
def create_events(sender, instance, **kwargs):
    end = datetime.datetime.now()
    end = end.replace(hour=23, minute=59)
    for user in instance.users.all():
        Event.objects.create(user=user,
                             description=sender.description,
                             summary=sender.title,
                             location="—",
                             end=end,
                             event_type=4
                             )
        print("create")


TYPES = (
    (0, "RADIO"),
    (1, "TEXT"),
    (2, "MULTPLY")
)


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.TextField(max_length=1000)
    typo = models.IntegerField(choices=TYPES, default=1)
    # Should be separated using ::
    choices = models.TextField(max_length=2000, blank=True)
    extra_placeholder = models.TextField(max_length=1000, default="")
    image = models.ImageField(upload_to="surveys", default="lk/static/images/noimg.jpg")


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Should be separated using ',' if Multiply
    answer = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def parse_answers(self):
        if self.question.typo == 2:
            return self.answer.split(sep=',')
        return self.answer

    def __str__(self):
        return "Ответ пользователя " + str(self.user.username) + " на вопрос из теста " + \
               str(self.question.survey.title)


class SurveyAnswer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer, blank=True)
    file = models.FileField(upload_to="user_surveys", blank=True, max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Ответ пользователя " + self.user.username + " на тест " + self.survey.title

    def save(self, *args, **kwargs):
        answers = Answer.objects.filter(question__survey=self.survey,
                                        user=self.user)
        super().save(*args, **kwargs)
        for answer in answers:
            self.answers.add(answer)
        super().save()
        if '№1' in self.survey.title:
            up = UserProfile.objects.get(user=self.user)
            up.isSurvey1 = True
            up.save()
        elif '№2' in self.survey.title:
            up = UserProfile.objects.get(user=self.user)
            up.isSurvey2 = True
            up.save()
        elif '№0' in self.survey.title:
            up = UserProfile.objects.get(user=self.user)
            up.isSurvey0 = True
            up.save()
        elif 'роль' in self.survey.title:
            up = UserProfile.objects.get(user=self.user)
            up.isStatus = True
            answer = self.answers.all()[-1]
            print(answer.answer)
            if answer.answer == 'Врач':
                up.status = 1
            elif answer.answer == 'Пациент':
                up.status = 0
            elif answer.answer == 'Родственник':
                up.status = 2
            up.save()
        process_test(self)
        self.process_answers()

    # @postpone
    def process_answers(self):
        df = pd.DataFrame(columns=['Вопрос', 'Ответ'])
        path = media + '/user_surveys/'
        for answer in self.answers.all():
            df = df.append({"Вопрос": answer.question.question,
                            "Ответ": answer.answer}, ignore_index=True)
        name = path + "Answers_" + str(self.user.pk) + "_" + str(self.survey.title.split()[1]) + "_" \
               + str(datetime.date.today()) + ".xlsx"
        df.to_excel(os.path.abspath(name), engine='openpyxl')
        self.file.name = name
        super().save()
        dr = DataRecording()
        dr.file.name = name
        dr.user = self.user
        dr.name = "Ответы на тест " + str(self.survey.title)
        dr.save()
