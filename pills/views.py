from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Pill, AssignedPill
from .serializers import PillSerializer


@api_view(['POST'])
def create_pill_assigment(request):
    """
    Creates pill assigment. Shoud have header 'user' with pk of user instance or field name, header 'pill' with pk of pill instance:<br>
    <b>Sample</b>:<br>
    {"name": "fedor",<br>
    "pill": "1"}<br>
    {"user": 4,<br>
    "pill": "1"}<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=request.data['user'])
        except KeyError:
            user = User.objects.get(username=request.data['name'])
        pill = Pill.objects.get(pk=request.data['pill'])
        try:
            AssignedPill.objects.create(user=user, pill=pill)
            return Response({"message": "Created"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['GET'])
def get_pills_list(request):
    """
    Returns pills list
    :param request:
    :return:
    """
    pills = Pill.objects.all()
    serializer = PillSerializer(pills, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def view_assigned_pills(request):
    """
    Returns assigned pills to user. Should have header 'user' or header "name".<br> <b>Samples:</b><br>
    {"user": 5}<br>
    {"name": "fedor"}<br>
    :param request:
    :return:
    """
    try:
        user = User.objects.get(pk=request.data['user'])
    except KeyError:
        user = User.objects.get(username=request.data['name'])
    assignee = AssignedPill.objects.filter(user=user)
    pills = []
    for rec in assignee:
        pills.append(rec.pill)
    serializer = PillSerializer(pills, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_pill(request):
    """
    Creates pill. Should have fields:<br>
    <b>Sample</b>:<br>
    {<br>
        "title": "Талбетка",<br>
        "info": "вываыва",<br>
        "dosege": "вдлалыдавтьы",<br>
        "time_out": "2021-05-06",<br>
        "time1": "16:00:00",<br>
        "time2": null,<br>
        "time3": null,<br>
        "time4": null,<br>
        "time5": null,<br>
        "extra": "ываыа",<br>
        "is_taken": true,<br>
        "typo": 1<br>
    }<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        serializer = PillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Pill created!"})
        else:
            return Response({"message": "Error!",
                             "errors": serializer.errors})
    else:
        return Response({"message": "Method not allowed!"})
