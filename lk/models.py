import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from diagnostic.models import Event

TEST = True

GENDER = (
    (0, "MALE"),
    (1, "FEMALE")
)

STATUS = (
    (0, "Врач"),
    (1, "Пациент"),
    (2, "Тестировщик"),
    (3, "Исследователь")
)


class UserProfile(models.Model):
    """
    Extended user model
    """
    # Ссылка на объект пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Имя
    name = models.CharField(max_length=50, blank=True)
    # Фамилия
    vorname = models.CharField(max_length=50, blank=True)
    # Отчество
    fathername = models.CharField(max_length=50, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    age = models.DateField(default=datetime.date(2000, 1, 1))
    parkinson = models.DateField(default=datetime.date(2000, 1, 1))
    # Статус в проекте — врач, пациент, тестировщик...
    status = models.IntegerField(choices=STATUS, default=0)
    # Опыт
    exp = models.IntegerField(default=0)
    # Флаг, указывающий на заполненные дополнительные поля
    isFull = models.BooleanField(default=False)
    # Город проживания
    city = models.CharField(max_length=50, blank=True)
    # URL на личную страницу
    slug = models.SlugField(null=True)
    # Avatar
    avatar = models.ImageField(upload_to="avatars", default="lk/static/images/noimg.jpg")
    send_push = models.BooleanField(default=True)

    def __str__(self):
        return "%s's profile" % self.user

    def get_absolute_url(self):
        """
        Makes slug
        :return: absolute url with slug
        """
        return reverse('profile_detail', kwargs={'slug': self.slug})


def create_user_profile(sender, instance, created, **kwargs):
    """
    This function will create UserProfile parallel with new User
    :param sender: NOT_USED
    :param instance: User object
    :param created: NOT_USED
    :param kwargs: User args
    :return:
    """
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)
        profile.slug = slugify(profile.user.get_username())
        profile.save()
        if TEST:
            Event.objects.create(description="Снимок в полный рост",
                                 summary="Снять себя в полный рост на хорошую камеру",
                                 location="SPB",
                                 end=datetime.datetime.now() + datetime.timedelta(hours=5),
                                 user=instance,
                                 event_type=3)
            Event.objects.create(description="Пройти тест",
                                 summary="Пройти тест 'Сложные виды поведения'",
                                 location="SPB",
                                 end=datetime.datetime.now() + datetime.timedelta(hours=5),
                                 user=instance,
                                 survey_pk=2,
                                 event_type=4)
            Event.objects.create(description="Загрузить историю болезни",
                                 summary="Загрузить файл в раздел загрузки",
                                 location="SPB",
                                 end=datetime.datetime.now() + datetime.timedelta(hours=5),
                                 user=instance,
                                 survey_pk=2,
                                 event_type=0)


post_save.connect(create_user_profile, sender=User)


class DiaryRecording(models.Model):
    """
    Diary recording model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=50, blank=True)
    text = models.CharField(max_length=2000, blank=True)
    published = models.DateTimeField(default=timezone.now)


class NewsRecording(models.Model):
    """
    News recording model
    """
    header = models.CharField(max_length=50, blank=True)
    text = models.CharField(max_length=2000, blank=True)
    published = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='news')
