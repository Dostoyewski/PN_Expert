from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from .decorators import postpone
from .pose_detector import handle_video


class Competition(models.Model):
    """
    Competiton model class
    """
    # Название испытания
    header = models.CharField(max_length=50, blank=True)
    # текстовое описание
    text = models.CharField(max_length=2000, blank=True)
    # Референсное видео
    # video_ref = models.FileField(upload_to="video_ref", blank=True)
    video_ref = models.CharField(max_length=2000, blank=True)
    # Количество exp за выполнение
    exp = models.IntegerField(default=100)
    # URL на страницу
    slug = models.SlugField(null=False, unique=True, default='123')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.header)
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def get_absolute_url(self):
        """
        Makes slug
        :return: absolute url with slug
        """
        return reverse('profile_detail', kwargs={'slug': self.slug})


class CompetitionRecording(models.Model):
    """
    Video recording with trajectory and status
    """
    published = models.DateTimeField(default=timezone.now)
    # user video
    video = models.FileField(upload_to="user_videos", blank=True)
    trajectory = models.TextField(default='')
    # Video with trajectory
    recognition = models.FileField(upload_to="user_videos_recogned", blank=True)
    # ref to user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ref to competition instance
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    # Flag if is recognized
    recognized = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.process_video()

    # TODO: change PoseDetector to MP_ANN
    @postpone
    def process_video(self):
        output, points = handle_video(self.video.name)
        self.trajectory = str(points)
        self.recognition.name = output
        self.recognized = True
        super().save()
