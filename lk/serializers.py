from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['status', 'avatar', 'user', 'slug', 'id']


class UserProfileAPISerializer(serializers.ModelSerializer):
    """
    UserProfile serializer
    """

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileAvatarSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["avatar"]
