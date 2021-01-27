from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from webpush import send_user_notification


@api_view(['POST'])
@csrf_exempt
@login_required
def send_push(request):
    """
    This function gets JSON with body and head, than pushes message
    :param request:
    :return: JSONResponse with status
    {"name": "admin",
    "head": "asd",
    "body": "asd"}
    {"name": "admin",
    "head": "Test message",
    "body": "Test message",
    "url": "example.com",
    "icon": "https://i.imgur.com/dRDxiCQ.png"}
    """
    try:
        data = request.data
        url = None
        try:
            url = data['url']
            icon = data['icon']
            use_full_shema = True
        except KeyError:
            use_full_shema = False
        try:
            user_id = data['id']
            user = get_object_or_404(User, pk=user_id)
        except KeyError:
            user_name = data['name']
            user = get_object_or_404(User, username=user_name)
        if use_full_shema:
            send_to_user(data['head'], data['body'], user, icon, url)
        else:
            payload = {'head': data['head'], 'body': data['body']}
            send_user_notification(user=user, payload=payload, ttl=1000)
        return JsonResponse(status=200, data={"message": "Web push successful"})
    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})


def send_to_user(head, body, user, icon="https://i.imgur.com/dRDxiCQ.png", url="https://www.example.com"):
    """
    This function will send push-notification to user
    :param head: HEAD of notification
    :type head: text
    :param body: BODY of the message
    :type body: text
    :param user: User object, that wil see this message
    :type user: User object
    :param icon: icon for notification
    :param url: notification-URL
    :return:
    """
    payload = {'head': head, 'body': body,
               "icon": icon, "url": url}
    send_user_notification(user=user, payload=payload, ttl=1000)
