import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

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
    (0, 'Мероприятие'),
    (1, 'Прием лекарств'),
    (2, 'Видео тест'),
    (3, 'Отправка фотографии'),
    (4, 'Опрос'),
)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default="")
    summary = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100, default="")
    start = models.DateTimeField(default=datetime.datetime.now)
    end = models.DateTimeField(default=datetime.datetime.now)
    event_type = models.IntegerField(choices=TYPES, default=0)
    survey_pk = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        create_event(summary=self.summary, location=self.location, description=self.description,
                     start=self.start.strftime('%Y-%m-%dT%H:%M:%S-23:59'),
                     end=self.end.strftime('%Y-%m-%dT%H:%M:%S-23:59'),
                     attendee=[{'email': self.user.email}])
        super().save(*args, **kwargs)


class DataRecording(models.Model):
    file = models.FileField(upload_to="user_files", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="File", max_length=100)
    date = models.DateTimeField(auto_now_add=True, blank=True)


# @receiver(post_save, sender=DataRecording)
# def update_data(sender, instance, **kwargs):
#     instance.date = timezone.now()
#     instance.save()


class DailyActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    steps = models.IntegerField(default=0)
    activity = models.CharField(max_length=1000)
    standing = models.FloatField(default=0.5)
    sitting = models.FloatField(default=0.1)
    liing = models.FloatField(default=0.1)
    upstairs = models.FloatField(default=0.1)
    downstairs = models.FloatField(default=0.1)
