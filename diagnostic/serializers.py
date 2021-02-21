from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.Serializer):
    """
    DiaryRecording serializer
    """
    description = serializers.CharField(max_length=1000)
    summary = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=100)
    start = serializers.CharField(max_length=100)
    end = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.header = validated_data.get('header', instance.header)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
