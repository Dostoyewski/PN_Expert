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


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default="")
    summary = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100, default="")
    start = models.CharField(max_length=100, default='2021-02-23T09:00:00-07:00')
    end = models.CharField(max_length=100, default='2021-02-23T09:00:00-07:00')

    def save(self, *args, **kwargs):
        create_event(summary=self.summary, location=self.location, description=self.description,
                     start=self.start, end=self.end, attendee=[{'email': self.user.email}])
        super().save(*args, **kwargs)
