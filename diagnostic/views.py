from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer


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
