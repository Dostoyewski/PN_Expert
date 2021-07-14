from allauth.account.admin import EmailAddress
from rest_framework import serializers, fields
from rest_framework.serializers import ModelSerializer

from .models import DiaryRecording, NewsRecording, UserProfile, TREMOR, StepsCounter, HADS_Result, HADS_Alarm


class DiaryRecordingSerializer(serializers.ModelSerializer):
    """
    DiaryRecording serializer
    """
    tremor = fields.MultipleChoiceField(choices=TREMOR)
    brake = fields.MultipleChoiceField(choices=TREMOR)

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
        exclude = ['avatar', 'user', 'slug', 'id']


class UserProfileAPISerializer(serializers.ModelSerializer):
    """
    UserProfile serializer
    """
    email_confirmed = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        # fields = ['user', 'name', 'vorname', 'fathername', 'gender', 'age',
        #           'parkinson', 'status', 'exp', 'isFull', 'city',
        #           'slug', 'avatar', 'send_push', 'email_confirmed']
        fields = '__all__'

    def get_email_confirmed(self, instance):
        return EmailAddress.objects.get(user=instance.user).verified


class UserProfileAvatarSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["avatar"]


class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepsCounter
        fields = '__all__'


class HADSSerializer(serializers.ModelSerializer):
    class Meta:
        model = HADS_Result
        fields = '__all__'


class ALARMSerializer(serializers.ModelSerializer):
    class Meta:
        model = HADS_Alarm
        fields = '__all__'
