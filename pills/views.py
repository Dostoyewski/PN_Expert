from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Pill, AssignedPill
from .serializers import PillSerializer, AssignedPillSerializer


@api_view(['POST'])
def create_pill_assigment(request):
    """
    Creates pill assigment. Shoud have header 'user' with pk of user instance or field name, header 'pill' with pk of pill instance:<br>
    <b>Sample</b>:<br>
    {"user": 4,<br>
    "pill": "1",<br>
    "dosege": "тест",<br>
    "time_out": "2021-05-06",<br>
    "extra": "тест",<br>
    "is_taken": true,<br>
    "time": "12:00::14:00"
    }<br>
    {"name": "fedor",<br>
    "pill": "1",<br>
    "dosege": "тест",<br>
    "time_out": "2021-05-06",<br>
    "extra": "тест",<br>
    "is_taken": true,<br>
    "time": "12:00::14:00"
    }<br>
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
            AssignedPill.objects.create(user=user,
                                        pill=pill,
                                        dosege=request.data['dosege'],
                                        time_out=request.data['time_out'],
                                        extra=request.data['extra'],
                                        is_taken=request.data['is_taken'],
                                        time=request.data['time'],
                                        )
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
    serializer2 = AssignedPillSerializer(assignee, many=True)
    data_pills = serializer.data
    data_assignee = serializer2.data
    for i, rec in enumerate(list(data_pills)):
        rec['time_out'] = data_assignee[i]['time_out']
        rec['is_taken'] = data_assignee[i]['is_taken']
        rec['dosege'] = data_assignee[i]['dosege']
        rec['extra'] = data_assignee[i]['extra']
        rec['time'] = data_assignee[i]['time']
        rec['time_taken'] = data_assignee[i]['time_taken']
    return Response(data_pills)


@api_view(['POST'])
def create_pill(request):
    """
    Creates pill. Should have fields:<br>
    <b>Sample</b>:<br>
    {<br>
        "id": 1,<br>
        "title": "Тестовая таблетка",<br>
        "info": "тест",<br>
        "dosege": "тест",<br>
        "time_out": "2021-05-06",<br>
        "time": "",<br>
        "extra": "тест",<br>
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


@api_view(['POST'])
def delete_pill_assigment(request):
    """
    Deletes pill assigment. Shoud have header 'user' with pk of user instance or field name, header 'pill' with pk of pill instance:<br>
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
            objs = AssignedPill.objects.filter(user=user, pill=pill)
            for obj in objs:
                obj.delete()
            return Response({"message": "Deleted!"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def mark_as_old_assigment(request):
    """
    Marks assigment as is_taken = False. Shoud have header 'user' with pk of user instance or field name, header 'pill' with pk of pill instance:<br>
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
            objs = AssignedPill.objects.filter(user=user, pill=pill)
            for obj in objs:
                obj.is_taken = not obj.is_taken
                obj.save()
            return Response({"message": "Marked as taken!"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def update_time_taken(request):
    """
    Updates taken time in PillAssigment. Should have headers 'time' and 'id' with obj pk.
    <br>
    <b>Sample:</b><br>
    {"pill_id": 5,<br>
    "user_id": 1,<br>
    "time": "12:00"}<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        assigments = AssignedPill.objects.filter(pill_id=request.data['pill_id'],
                                                 user_id=request.data['user_id'])
        for assigment in assigments:
            assigment.time_taken += str(request.data['time']) + "::"
            assigment.save()
        return Response({"message": "Updated"}, status=status.HTTP_200_OK)
        # except:
        #     return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def reset_time_taken(request):
    """
    Updates taken time in PillAssigment. Should have headers 'time' and 'id' with obj pk.
    <br>
    <b>Sample:</b><br>
    {"pill_id": 5,<br>
    "user_id": 1}<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        try:
            assigments = AssignedPill.objects.filter(pill_id=request.data['pill_id'],
                                                     user_id=request.data['user_id'])
            for assigment in assigments:
                assigment.time_taken = ""
                assigment.save()
            return Response({"message": "Reseted"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Method not allowed!"})
