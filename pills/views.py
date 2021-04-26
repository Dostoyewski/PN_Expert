from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Pill, AssignedPill


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
