from rest_framework import serializers

from .models import CompetitionRecording, Competition


class CompetitionRecordingSerializer(serializers.Serializer):
    """
    CompetitionRecording serializer
    """

    class Meta:
        model = CompetitionRecording
        exclude = ''


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'
