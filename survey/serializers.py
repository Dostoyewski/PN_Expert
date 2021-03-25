from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """
    Question serializer
    """

    class Meta:
        model = Question
        fields = '__all__'

        def create(self, validated_data):
            return Question.objects.create(**validated_data)


class AnswerSerializer(serializers.ModelSerializer):
    """
    Question serializer
    """

    class Meta:
        model = Question
        fields = '__all__'

        def create(self, validated_data):
            return Question.objects.create(**validated_data)
