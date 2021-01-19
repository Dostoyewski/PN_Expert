from rest_framework import serializers

from .models import CompetitionRecording, Competition


class CompetitionRecordingSerializer(serializers.Serializer):
    """
    CompetitionRecording serializer
    """
    published = serializers.DateTimeField()

    def create(self, validated_data):
        return CompetitionRecording.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.header = validated_data.get('header', instance.header)
        instance.save()
        return instance


class CompetitionSerializer(serializers.Serializer):
    header = serializers.CharField(max_length=50)
    text = serializers.CharField(max_length=2000)
    video_ref = serializers.CharField()
    exp = serializers.IntegerField()
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Competition.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.header = validated_data.get('header', instance.header)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
