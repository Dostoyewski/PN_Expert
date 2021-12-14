import datetime
import time

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from googleapiclient.errors import HttpError

from video_proc.decorators import postpone
from .google_sync import create_event


class Game(models.Model):
    """
    Competiton model class
    """
    # Название испытания
    header = models.CharField(max_length=50, blank=True)
    # текстовое описание
    text = models.CharField(max_length=2000, blank=True)
    # Ссылка на материал для тестирования
    materials = models.CharField(max_length=2000, blank=True)
    # Количество exp за выполнение
    exp = models.IntegerField(default=100)
    # URL на страницу
    slug = models.SlugField(null=False, unique=True, default='123')
    # ref to user instance
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.header)
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def get_absolute_url(self):
        """
        Makes slug
        :return: absolute url with slug
        """
        return reverse('profile_detail', kwargs={'slug': self.slug})


class GameRecording(models.Model):
    """
    Recording with games/teste
    """
    published = models.DateTimeField(default=timezone.now)
    # ref to user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ref to competition instance
    competition = models.ForeignKey(Game, on_delete=models.CASCADE)
    data = models.CharField(max_length=1000, default=" ")


TYPES = (
    (0, 'Документ'),
    (1, 'Графический тест'),
    (2, 'Видеотест'),
    (3, 'Фототест'),
    (4, 'Опрос'),
    (5, 'Игра')
)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=5000, default="")
    summary = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=2000, default="")
    start = models.DateTimeField(default=datetime.datetime.now)
    end = models.DateTimeField(default=datetime.datetime.now)
    event_type = models.IntegerField(choices=TYPES, default=0)
    survey_pk = models.IntegerField(default=0)
    isDone = models.BooleanField(default=False)
    # Тектосовое описание для оценки видео
    text_r0 = models.CharField(default="", max_length=2000)
    text_r1 = models.CharField(default="", max_length=2000)
    text_r2 = models.CharField(default="", max_length=2000)
    text_r3 = models.CharField(default="", max_length=2000)
    text_r4 = models.CharField(default="", max_length=2000)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if type(self.start) is not datetime.datetime:
            self.start = datetime.datetime.strptime(self.start, '%Y-%m-%dT%H:%M:%S')
        if type(self.end) is not datetime.datetime:
            self.end = datetime.datetime.strptime(self.end, '%Y-%m-%dT%H:%M:%S')
        while True:
            try:
                create_event(summary=self.summary, location=self.location, description=self.description,
                             start=self.start.strftime('%Y-%m-%dT%H:%M:%S-23:59'),
                             end=self.end.strftime('%Y-%m-%dT%H:%M:%S-23:59'),
                             attendee=[{'email': self.user.email}])
                break
            except HttpError:
                time.sleep(5)
        note = PushNotification(event=self, is_shown=False)
        note.save()


DOCTOR_TYPES = (
    (0, "Оценивание видео"),
    (1, "Оценивание фотографии"),
    (2, "Оценивание фототеста")
)

TYPES_FILES = (
    (0, "Обследование"),
    (1, "Операция"),
    (2, "Тест"),
    (3, "Препараты"),
    (4, "Анализы"),
    (5, "Другое")
)

MEDIA_TYPES = (
    (0, "Видео"),
    (1, "Фотогафия"),
    (2, "Фототест")
)


class DataRecording(models.Model):
    file = models.FileField(upload_to="user_files", blank=True, max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="File", max_length=100)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    typo = models.IntegerField(choices=TYPES_FILES, default=5)


class MediaRecording(models.Model):
    event_id = models.ForeignKey(Event, default=2111, on_delete=models.CASCADE)
    file = models.FileField(upload_to="user_files", blank=True, max_length=500)
    description = models.CharField(default="", max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="File", max_length=100)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    typo = models.IntegerField(choices=MEDIA_TYPES, default=0)
    time = models.FloatField(default=0)
    mark = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        from lk.models import UserProfile
        super().save(*args, **kwargs)
        info = ""
        if self.typo == 0:
            info = "видеотеста по системе UPDRS"
        elif self.typo == 1:
            info = "фотографии пациента по системе UPDRS"
        elif self.typo == 2:
            info = "фототеста"
        doctor = UserProfile.objects.get(user=self.user).doctor
        DoctorEvent.objects.create(description="Оценить результаты",
                                   summary="Оценить результаты " + info,
                                   end=datetime.datetime.now() + datetime.timedelta(days=1),
                                   user=doctor,
                                   event_type=self.typo,
                                   video=self,
                                   patient=self.user)


class DoctorEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    description = models.CharField(max_length=5000, default="")
    summary = models.CharField(max_length=100, default="")
    video = models.ForeignKey(MediaRecording, on_delete=models.CASCADE)
    start = models.DateTimeField(default=datetime.datetime.now)
    end = models.DateTimeField(default=datetime.datetime.now)
    event_type = models.IntegerField(choices=DOCTOR_TYPES, default=0)
    isDone = models.BooleanField(default=False)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient',
                                default=1)
    info = models.CharField(max_length=1000, default="—")
    r0 = models.CharField(max_length=5000, default="")
    r1 = models.CharField(max_length=5000, default="")
    r2 = models.CharField(max_length=5000, default="")
    r3 = models.CharField(max_length=5000, default="")
    r4 = models.CharField(max_length=5000, default="")

    def save(self, *args, **kwargs):
        event = self.video.event_id
        self.r0 = event.text_r0
        self.r1 = event.text_r1
        self.r2 = event.text_r2
        self.r3 = event.text_r3
        self.r4 = event.text_r4
        super().save(*args, **kwargs)
        if type(self.start) is not datetime.datetime:
            self.start = datetime.datetime.strptime(self.start, '%Y-%m-%dT%H:%M:%S')
        if type(self.end) is not datetime.datetime:
            self.end = datetime.datetime.strptime(self.end, '%Y-%m-%dT%H:%M:%S')
        self.create_gevent()
        # note = PushNotification(event=self, is_shown=False)
        # note.save()

    @postpone
    def create_gevent(self):
        while True:
            try:
                create_event(summary=self.summary, location="SPB", description=self.description,
                             start=self.start.strftime('%Y-%m-%dT%H:%M:%S-23:59'),
                             end=self.end.strftime('%Y-%m-%dT%H:%M:%S-23:59'),
                             attendee=[{'email': self.user.email}])
                break
            except HttpError:
                time.sleep(5)


class DailyActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    steps = models.IntegerField(default=0)
    activity = models.CharField(max_length=1000)
    standing = models.FloatField(default=0.5)
    sitting = models.FloatField(default=0.1)
    liing = models.FloatField(default=0.1)
    upstairs = models.FloatField(default=0.1)
    downstairs = models.FloatField(default=0.1)


class StartEvent(models.Model):
    """
    Event, который назначается всем пользователям при старте
    """
    description = models.CharField(max_length=2000, default="")
    summary = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=2000, default="")
    day_delta = models.IntegerField(default=2)
    event_type = models.IntegerField(choices=TYPES, default=0)
    survey = models.ForeignKey('survey.Survey', on_delete=models.CASCADE)


SHEDULE_TYPE = (
    (0, 'Ежедневно'),
    (1, 'Раз в неделю'),
    (2, 'Раз в месяц'),
    (3, 'Раз в квартал')
)


class StartShedule(models.Model):
    """
    Объект с расписанием, который создается всем пользователям при старте.
    """
    run_interval = models.IntegerField(choices=SHEDULE_TYPE, default=0)
    survey = models.ForeignKey('survey.Survey', on_delete=models.CASCADE)
    description = models.TextField(max_length=2000, default=" ")


class MessageShedule(models.Model):
    """
    Объект с расписанием сообщений, который создается всем пользователям при старте.
    """
    run_interval = models.IntegerField(choices=SHEDULE_TYPE, default=0)
    message = models.TextField(default=" ")
    typo = models.IntegerField(choices=TYPES)
    forall = models.BooleanField(default=False)
    location = models.CharField(max_length=2000, default=" ")
    day_delta = models.IntegerField(default=0)
    description = models.CharField(max_length=2000, default=" ")
    r0 = models.CharField(max_length=5000, default="")
    r1 = models.CharField(max_length=5000, default="")
    r2 = models.CharField(max_length=5000, default="")
    r3 = models.CharField(max_length=5000, default="")
    r4 = models.CharField(max_length=5000, default="")


class PushNotification(models.Model):
    """
    Push notifications for our mobile APP
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_shown = models.BooleanField(default=False)
