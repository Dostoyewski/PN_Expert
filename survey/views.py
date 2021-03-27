import datetime

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from diagnostic.models import Event
from .models import Question, Answer, Survey
from .serializers import QuestionSerializer, AnswerSerializer, SurveySerializer


@api_view(['POST'])
def get_survey(request):
    """
    Returns all questions in survey. Request should contain header <b>'survey'</b> with survey.pk<br>
    <b>Sample</b><br>
    {"survey": 1}
    :param request:
    :return:
    """
    if request.method == 'POST':
        survey_id = request.data['survey']
        questions = Question.objects.filter(survey__pk=survey_id)
        return Response({"data": QuestionSerializer(questions, many=True).data})
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def create_question(request):
    """
    Creates question. Should contain all question fields:<br>
    survey: survey_pk<br>
    question: text with question<br>
    typo: type of question: 0 — radio, 1 — text, 2 — multiply<br>
    choices: choices for types 0, 2. Should be separated using ::<br>
    <b>Sample</b>:<br>
    {"survey": 1,<br>
     "question": "Test data",<br>
     "typo": "0",<br>
     "choices": "Answer1::Answer2::Answer3"}<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Question created!"})
        else:
            return Response({"message": "Error!"})
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def create_answer(request):
    """
    Creates answer. Should contain all answer fields:<br>
    answer: text. If choices, separate with ::<br>
    question: question_pk<br>
    user: user_pk<br>
    <b>Sample</b>:<br>
    {"answer": "some text",<br>
     "question": 1,<br>
     "user": 5}<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Answer created!"})
        else:
            return Response({"message": "Error!"})
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def create_survey(request):
    """
    Creates survey. Should contain all survey fields:<br>
    description: text.<br>
    points: integer<br>
    users: users_pk<br>
    num_q: num of question<br>
    title: num of question<br>
    <b>Sample</b>:<br>
    {"users": [5, 6, 7],<br>
     "points": 1,<br>
     "num_q": 5,<br>
     "title": "TEST",<br>
     "description": "logit function"}<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            for i in request.data['users']:
                user = User.objects.get(pk=i)
                end = datetime.datetime.now()
                end = end.replace(hour=23, minute=59)
                Event.objects.create(user=user,
                                     description=request.data['description'],
                                     summary=request.data['title'],
                                     location="—",
                                     end=end,
                                     event_type=4
                                     )
            return Response({"message": "Survey created!"})
        else:
            return Response({"message": "Error!"})
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def get_answer(request):
    """
    Returns answer. Should contain fields user or username and survey:<br>
    user: user_pk<br>
    survey: survey_pk<br>
    username: username<br>
    <b>Sample</b>:<br>
    {"user": 5,<br>
     "survey": 2}<br>
    {"username": "fedor",<br>
     "survey": 2}<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=request.data['user'])
        except KeyError:
            user = User.objects.get(username=request.data['username'])
        survey = Survey.objects.get(pk=request.data['survey'])
        answers = Answer.objects.filter(user=user, question__survey=survey)
        questions = Question.objects.filter(survey=survey)
        serializer = AnswerSerializer(answers, many=True)
        return Response({"answers": serializer.data,
                         "questions": QuestionSerializer(questions, many=True).data})
    else:
        return Response({"message": "Method not allowed!"})
