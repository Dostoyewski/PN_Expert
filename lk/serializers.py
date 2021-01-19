from rest_framework import serializers

from .models import DiaryRecording, NewsRecording, UserProfile


class DiaryRecordingSerializer(serializers.Serializer):
    """
    DiaryRecording serializer
    """
    header = serializers.CharField(max_length=50)
    text = serializers.CharField(max_length=2000)
    published = serializers.DateTimeField()

    def create(self, validated_data):
        return DiaryRecording.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.header = validated_data.get('header', instance.header)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class NewsRecordingSerializer(serializers.Serializer):
    header = serializers.CharField(max_length=50)
    text = serializers.CharField(max_length=2000)
    published = serializers.DateTimeField()
    img = serializers.ImageField()

    def create(self, validated_data):
        return NewsRecording.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.header = validated_data.get('header', instance.header)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class UserProfileSerializer(serializers.Serializer):
    """
    UserProfile serializer
    """
    name = serializers.CharField(max_length=50)
    # Фамилия
    vorname = serializers.CharField(max_length=50)
    # Отчество
    fathername = serializers.CharField(max_length=50)
    gender = serializers.IntegerField()
    age = serializers.DateField()
    # Статус в проекте — врач, пациент, тестировщик...
    status = serializers.IntegerField()
    # Город проживания
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.vorname = validated_data.get('vorname', instance.vorname)
        instance.save()
        return instance
