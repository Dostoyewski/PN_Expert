from rest_framework import serializers

from .models import Event, DataRecording


class EventSerializer(serializers.Serializer):
    """
    DiaryRecording serializer
    """
    description = serializers.CharField(max_length=1000)
    summary = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=100)
    start = serializers.CharField(max_length=100)
    end = serializers.CharField(max_length=100)
    event_type = serializers.IntegerField()
    survey_pk = serializers.IntegerField()

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.header = validated_data.get('header', instance.header)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class DataRecordingFileSerializer(serializers.Serializer):
    """
    DiaryRecording serializer
    """
    file = serializers.FileField()

    def create(self, validated_data):
        return DataRecording.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.header = validated_data.get('header', instance.header)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class DataRecordingSerializer(serializers.ModelSerializer):
    """
    Drecording serializer
    """

    class Meta:
        model = DataRecording
        fields = '__all__'

        def create(self, validated_data):
            return DataRecording.objects.create(**validated_data)


class DataRecordingCreateSerializer(serializers.ModelSerializer):
    """
    Drecording serializer
    """

    class Meta:
        model = DataRecording
        fields = ('file', 'user', 'name')

        def create(self, validated_data):
            return DataRecording.objects.create(**validated_data)


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRecording
        fields = ('file', 'user')
