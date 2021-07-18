from datetime import datetime, date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from lk.models import UserProfile
from .forms import DataRecordingForm
from .models import Event, DataRecording, DailyActivity, PushNotification
from .serializers import EventSerializer, DataRecordingSerializer, \
    DataRecordingCreateSerializer, PushSerializer


# TODO: Add username to pk API
# TODO: Add security checks
# TODO: Fix submitting API

@login_required()
@api_view(['POST'])
def create_event(request):
    """
    Creates event for user
    {"username": "fedor",
    "description": "test Event",
    "summary": "test",
    "location": "SPB",
    "start": "2021-03-1T09:00:00-07:00",
    "end": "2021-03-1T18:00:00-07:00"}
    :param request:
    :return:
    """
    usr = User.objects.get(username=request.data['username'])
    Event.objects.create(description=request.data['description'],
                         summary=request.data['summary'],
                         location=request.data['location'],
                         start=request.data['start'],
                         end=request.data['end'],
                         user=usr)
    return Response({"message": "Ok"})


@login_required()
def get_all_events(request):
    usr = request.user
    events = Event.objects.filter(user=usr)
    return render(request, 'events.html', {'events': EventSerializer(events, many=True).data})


@login_required()
def load_file(request):
    user = request.user
    if request.method == 'POST':
        form = DataRecordingForm(request.POST, request.FILES)
        if form.is_valid():
            recording = DataRecording()
            recording.file = form.cleaned_data['file']
            recording.user = user
            recording.save()
            return HttpResponseRedirect(reverse('file_list'))

    else:
        form = DataRecordingForm()
    return render(request, 'load_file.html', {'form': form})


@login_required()
def file_list(request):
    user = request.user
    files = DataRecording.objects.filter(user=user)
    return render(request, 'file_list.html',
                  {'files': DataRecordingSerializer(files, many=True).data})


@login_required()
@api_view(['POST'])
def create_activity(request):
    """
    Creates event for user
    {"username": "fedor",
    "steps": 1000,
    "activity": "[12, 12, 12]",
    "standing": 0.5,
    "sitting": 0.1,
    "liing": 0.2,
    "upstairs": 0.4,
    "downstairs": 0.1}
    :param request:
    :return:
    """
    usr = User.objects.get(username=request.data['username'])
    DailyActivity.objects.create(user=usr, steps=request.data['steps'],
                                 activity=request.data['activity'], standing=request.data['standing'],
                                 sitting=request.data['sitting'], liing=request.data['liing'],
                                 upstairs=request.data['upstairs'],
                                 downstairs=request.data['downstairs'])
    return Response({"message": "Ok"})


@api_view(['POST'])
def get_user_events(request):
    """
    Get user events. Shoud have header 'user' with pk of user instance or header 'username' with username<br>
    <b>Samples</b>:<br>
    {"user": 5}<br>
    {"username": "fedor"}<br>
    <b>Event Types</b>:<br>
    0: 'Мероприятие',<br>
    1: 'Прием лекарств',<br>
    2: 'Видео тест',<br>
    3: 'Отправка фотографии',<br>
    4: 'Опрос',<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        try:
            events = Event.objects.filter(isDone=False, user__pk=request.data['user'])
            # TODO: remove this part with tomorrow events
            devents = Event.objects.filter(isDone=True, user__pk=request.data['user'],
                                           start__date=date.today())
        except KeyError:
            devents = Event.objects.filter(isDone=True, user__username=request.data['username'],
                                           start__date=date.today())
            events = Event.objects.filter(isDone=False,
                                          user__username=request.data['username'])
        return Response({"events": EventSerializer(events, many=True).data,
                         "done_events": EventSerializer(devents, many=True).data,
                         "message": "ok"})
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def get_event_by_date(request):
    """
    Get user events. Shoud have header 'user' with pk of user instance or header 'username' with username and header 'date<br>
    date should have format '%Y-%m-%d'<br>
    <b>Samples</b>:<br>
    {"user": 5,<br>
    "date": "2021-03-27"}<br>
    {"username": "luna_koly",<br>
    "date": "2021-03-28"}<br>
    <b>Event Types</b>:<br>
    0: 'Мероприятие',<br>
    1: 'Прием лекарств',<br>
    2: 'Видео тест',<br>
    3: 'Отправка фотографии',<br>
    4: 'Опрос',<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        date_req = datetime.strptime(request.data['date'], '%Y-%m-%d')
        try:
            events = Event.objects.filter(start__date=date_req, user__pk=request.data['user'])
        except KeyError:
            events = Event.objects.filter(start__date=date_req,
                                          user__username=request.data['username'])
        return Response({"events": EventSerializer(events, many=True).data,
                         "message": "ok"})
    else:
        return Response({"message": "Method not allowed!"})


class FileView(APIView):
    """
    Should contain fieds 'file' with a file, 'user' with user pk, 'name' with filename, 'typo' with file type
    """
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = DataRecordingCreateSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_user_files(request):
    """
    Get user files. Shoud have header 'user' with pk of user instance or header 'username' with username<br>
    <b>Samples</b>:<br>
    {"user": 5}<br>
    {"username": "admin"}<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        try:
            files = DataRecording.objects.filter(user__pk=request.data['user'])
        except KeyError:
            files = DataRecording.objects.filter(user__username=request.data['username'])
        return Response({"files": DataRecordingSerializer(files, many=True).data,
                         "message": "ok"})
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def mark_as_done(request):
    """
    Marks event as done. Shoud have header 'event' with pk of event instance<br>
    <b>Sample</b>:<br>
    {"event": 5}<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        try:
            event = Event.objects.get(pk=request.data['event'])
            event.isDone = True
            try:
                note = PushNotification.objects.get(event=event)
                note.is_shown = True
                note.save()
            except:
                pass
            event.save()
            return Response({"message": "ok"})
        except KeyError:
            return Response({"message": "Check your format!"})
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def get_user_notifications(request):
    """
    Returns all actual user notifications. Should have header 'user' with user id or header 'username'.<br>
    <b>Sample</b>:<br>
    {"user": 5}<br>
    {"username": "fedor"}<br>
    :param request:
    :return:
    """
    try:
        user = User.objects.get(pk=request.data['user'])
        notifications = PushNotification.objects.filter(event__user=user,
                                                        is_shown=False)
    except KeyError:
        user = User.objects.get(username=request.data['username'])
        notifications = PushNotification.objects.filter(event__user=user,
                                                        is_shown=False)
    payload = []
    for p in notifications:
        data = PushSerializer(p).data
        data['description'] = p.event.description
        data['summary'] = p.event.summary
        data['event_type'] = p.event.event_type
        data['start'] = str(p.event.start)
        data['end'] = str(p.event.end)
        payload.append(data)
    return Response({"push": payload})


@api_view(['POST'])
def mark_notification_as_shown(request):
    """
    Marks notification as shown. Should have header 'id' with notification id.<br>
    <b>Sample</b>:<br>
    {"id": 5}<br>
    :param request:
    :return:
    """
    try:
        note = PushNotification.objects.get(pk=request.data['id'])
        note.is_shown = True
        note.save()
        return Response({"message": "ok"})
    except:
        return Response({"message": "error"})


@api_view(['POST'])
def get_push_period(request):
    """
    Return period of push notifications. Should have header `user` or `username`<br>
    <b>Sample</b>:<br>
    {"user": 69}<br>

    :param request:
    :return:<br>
    (0, '1 час'),<br>
    (1, '3 часа'),<br>
    (2, '5 часов'),<br>
    (3, '7 часов')<br>
    """
    up = None
    try:
        user = User.objects.get(pk=request.data['user'])
        up = UserProfile.objects.get(user=user)
    except KeyError:
        user = User.objects.get(username=request.data['username'])
        up = UserProfile.objects.get(user=user)
    return Response({"period": up.reminders})
