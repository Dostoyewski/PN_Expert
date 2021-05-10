from rest_framework import serializers

from .models import CompetitionRecording, Competition, PhotoCompetition, PhotoCompetitionRecording


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


class PhotoCompetitionRecordingSerializer(serializers.Serializer):
    """
    CompetitionRecording serializer
    """

    class Meta:
        model = PhotoCompetitionRecording
        exclude = ''


class PhotoCompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoCompetition
        fields = '__all__'
