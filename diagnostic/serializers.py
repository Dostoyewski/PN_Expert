from rest_framework import serializers

from .models import Event, DataRecording, PushNotification, MediaRecording, DoctorEvent


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
    isDone = serializers.BooleanField()
    pk = serializers.IntegerField()

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


class MediaRecordingSerializer(serializers.ModelSerializer):
    """
    MediaRecoedinf serializer
    """

    class Meta:
        model = MediaRecording
        fields = '__all__'

        def create(self, validated_data):
            return MediaRecording.objects.create(**validated_data)


class DataRecordingCreateSerializer(serializers.ModelSerializer):
    """
    Drecording serializer
    """

    class Meta:
        model = DataRecording
        fields = ('file', 'user', 'name', 'typo')

        def create(self, validated_data):
            return DataRecording.objects.create(**validated_data)


class DoctorEventSeralizer(serializers.ModelSerializer):
    """
    Drecording serializer
    """
    rating = serializers.SerializerMethodField('process_rating')

    def process_rating(self, obj):
        dict = {}
        dict['0'] = obj.r0
        dict['1'] = obj.r1
        dict['2'] = obj.r2
        dict['3'] = obj.r3
        dict['4'] = obj.r4
        return dict

    class Meta:
        model = DoctorEvent
        fields = ['user', 'description', 'summary', 'video', 'start', 'end', 'event_type',
                  'isDone', 'patient', 'info', 'rating']

        def create(self, validated_data):
            return DoctorEvent.objects.create(**validated_data)


class MediaRecordingCreateSerializer(serializers.ModelSerializer):
    """
    Drecording serializer
    """
    class Meta:
        model = MediaRecording
        fields = ('file', 'user', 'name', 'typo', 'time', 'description', 'event_id')


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRecording
        fields = ('file', 'user')


class PushSerializer(serializers.ModelSerializer):
    """
    Drecording serializer
    """

    class Meta:
        model = PushNotification
        fields = '__all__'
