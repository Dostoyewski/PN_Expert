import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from push_notifications import send_user_notification


@require_POST
@csrf_exempt
def send_push(request):
    """
    This function gets JSON with body and head, than pushes message
    :param request:
    :return: JSONResponse with status
    """
    try:
        body = request.body
        data = json.loads(body)

        if 'head' not in data or 'body' not in data or 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})

        user_id = data['id']
        user = get_object_or_404(User, pk=user_id)
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


@login_required
@require_GET
def home(request):
    """
    This funciton represents the main page
    :param request:
    :return:
    """
    # send_to_user('INFO', 'This is the main page', get_object_or_404(User, pk=request.user.pk))
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    user = request.user
    return render(request, 'main/home.html', {user: user, 'vapid_key': vapid_key})
