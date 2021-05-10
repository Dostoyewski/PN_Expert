from allauth.account.admin import EmailAddress
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import DiaryRecording, NewsRecording, UserProfile


class DiaryRecordingSerializer(serializers.ModelSerializer):
    """
    DiaryRecording serializer
    """

    class Meta:
        model = DiaryRecording
        fields = '__all__'



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
    email_confirmed = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['user', 'name', 'vorname', 'fathername', 'gender', 'age',
                  'parkinson', 'status', 'exp', 'isFull', 'city',
                  'slug', 'avatar', 'send_push', 'email_confirmed']
        # fields = '__all__'

    def get_email_confirmed(self, instance):
        return EmailAddress.objects.get(user=instance.user).verified


class UserProfileAvatarSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["avatar"]
