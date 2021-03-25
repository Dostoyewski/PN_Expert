from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer, AnswerSerializer


@api_view(['POST'])
def get_survey(request):
    """
    Returns all questions in survey. Request should contain header <b>'survey'</b> with survey.pk<br>
    <b>Sample</b><br>
    {'survey': 1}
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
     "choices": "Answer1::Answer2::Answer3",<br>
     }
    :param request:
    :return:
    """
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        try:
            serializer.save()
            return Response({"message": "Question created!"})
        except:
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
     "user": 5,<br>
     }
    :param request:
    :return:
    """
    if request.method == 'POST':
        serializer = AnswerSerializer(data=request.data)
        try:
            serializer.save()
            return Response({"message": "Question created!"})
        except:
            return Response({"message": "Error!"})
    else:
        return Response({"message": "Method not allowed!"})
