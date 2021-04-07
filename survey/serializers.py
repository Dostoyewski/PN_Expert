from rest_framework import serializers

from .models import Question, Survey, Answer, SurveyAnswer


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
        model = Answer
        fields = '__all__'

        def create(self, validated_data):
            return Question.objects.create(**validated_data)


class SurveySerializer(serializers.ModelSerializer):
    """
    Survey serializer
    """

    class Meta:
        model = Survey
        fields = '__all__'

        def create(self, validated_data):
            return Question.objects.create(**validated_data)


class SurveyAnswerSerializer(serializers.ModelSerializer):
    """
    SurveyAnswer serializer
    """

    class Meta:
        model = SurveyAnswer
        fields = ['survey', 'user']

        def create(self, validated_data):
            return SurveyAnswer.objects.create(**validated_data)
