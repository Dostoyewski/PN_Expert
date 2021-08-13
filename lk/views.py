import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UserProfileForm
from .models import UserProfile, DiaryRecording, NewsRecording, StepsCounter, HADS_Result, HADS_Alarm, \
    SmileStats
from .serializers import DiaryRecordingSerializer, NewsRecordingSerializer, \
    UserProfileSerializer, UserProfileAPISerializer, UserProfileAvatarSerializer, StepsSerializer, HADSSerializer, \
    ALARMSerializer, SmileSerializer


# TODO: add API method for email —> pk
def profile(request, slug):
    """
    This function return user profile that contains slug
    :param request:
    :param slug: slug to UProfile
    :return: render
    """
    u_profile = get_object_or_404(UserProfile, slug=slug)
    return render(request, 'account_c.html', {'profile': u_profile})


@login_required()
def account(request):
    """
    way to account with ability to change user fields
    :param request:
    :return:
    """
    u_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            u_profile.name = form.cleaned_data['name']
            u_profile.vorname = form.cleaned_data['vorname']
            u_profile.fathername = form.cleaned_data['fathername']
            u_profile.gender = form.cleaned_data['gender']
            u_profile.age = form.cleaned_data['age']
            u_profile.status = form.cleaned_data['status']
            u_profile.city = form.cleaned_data['city']
            u_profile.avatar = form.cleaned_data['avatar']
            u_profile.isFull = True
            u_profile.save()
            return HttpResponseRedirect('/account/')

    else:
        init_data = UserProfileSerializer(u_profile).data
        init_data['avatar'] = u_profile.avatar
        form = UserProfileForm(initial=init_data)
    return render(request, 'account.html', {'profile': u_profile,
                                            'form': form})


@login_required()
@api_view(['POST'])
def update_params(request):
    """
    Used to update Users parameters, such as name, vorname and others
    :param request:
    :return:
    """
    if request.method == 'POST':
        u_profile = get_object_or_404(UserProfile, user=request.user)
        if 'name' in request.data:
            u_profile.name = str(request.data['name'])
        if 'vorname' in request.data:
            u_profile.vorname = str(request.data['vorname'])
        if 'fathername' in request.data:
            u_profile.fathername = str(request.data['fathername'])
        if 'status' in request.data:
            try:
                u_profile.status = int(request.data['status'])
            except ValueError:
                return Response({"message": "status should be INT!"})
        if 'city' in request.data:
            u_profile.city = str(request.data['city'])
        u_profile.save()
        return Response({"message": "Successfully updated!"})
    return Response({"message": "Method not allowed!"})


def news_list(request):
    """
    page with news list
    :param request:
    :return:
    """
    return render(request, 'news.html', {"recordings": NewsRecordingSerializer(NewsRecording.objects.all(),
                                                                               many=True).data})


@api_view(['POST'])
def create_diary_rec(request):
    """
    Creates diary recording.<br>
    <b>Sample:</b><br>
    {<br>
            "tremor": [2, 4, 5],<br>
            "brake": [0, 4],<br>
            "text": "test",<br>
            "stimulators": 0,<br>
            "user": 9<br>
        }<br>
    :param request:
    :return:
    """
    try:
        serializer = DiaryRecordingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(pk=request.data['user'])
            up = UserProfile.objects.get(user=user)
            up.isDiary = True
            up.save()
            return Response({"message": "ok"})
        else:
            return Response({"errors": serializer.errors})
    except:
        return Response({"message": "incorrect"})


@api_view(['POST'])
def get_diary_list(request):
    """
    Returns diary recordings, all or last. Should contain fields "user" or "username" and optional<br>
    field "last". If last exist it will be return only last recording.<br>
    <b>Sample:</b><br>
    {"user": 5,<br>
    "last": true}<br>
    {"username": "fedor"}
    :param request:
    :return:
    """
    try:
        user = User.objects.get(pk=request.data['user'])
    except KeyError:
        user = User.objects.get(username=request.data['username'])
    last = False
    try:
        if request.data['last']:
            last = True
    except KeyError:
        last = False
    if last:
        try:
            obj = DiaryRecordingSerializer(
                DiaryRecording.objects.filter(user=user).order_by('-id')[0]).data
        except IndexError:
            obj = {}
        return Response({"recordings": obj})
    else:
        return Response({"recordings": DiaryRecordingSerializer(DiaryRecording.objects.filter(user=user),
                                                                many=True).data})


def main_redirect_view(request):
    """
    redirects to main page
    :param request:
    :return:
    """
    return HttpResponseRedirect('/')


def home(request):
    """
    This funciton represents the main page
    :param request:
    :return:
    """
    if not request.user.is_anonymous:
        u_profile = get_object_or_404(UserProfile, user=request.user)
    else:
        u_profile = {'name': "Имя", 'vorname': "Фамилия"}
    return render(request, 'main.html', {"recordings": NewsRecordingSerializer(NewsRecording.objects.all(),
                                                                               many=True).data,
                                         'profile': u_profile})


@api_view(['POST'])
def get_user_info(request):
    """
    Get user info. Shoud have header 'user' with pk of user instance<br>
    <b>Sample</b>:<br>
    {"user": 5}<br>
    :param request:
    :return:
    """
    if request.method == 'GET':
        return Response({"profiles": UserProfileAPISerializer(UserProfile.objects.all(), many=True).data})
    elif request.method == 'POST':
        up = UserProfile.objects.get(user__pk=request.data['user'])
        return Response({"profiles": UserProfileAPISerializer(up).data})
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def get_user_id(request):
    """
    Get pk from email, should have field 'email' with user email.<br>
    <b>Sample:</b><br>
    {"email": "dostoyewski@yandex.ru"}
    :param request:
    :return:
    """
    if request.method == 'POST':
        user = User.objects.get(email=request.data['email'])
        return Response({"id": user.pk, "status": "ok"})
    else:
        return Response({"status": "fail"})


class UserAvatarUpload(APIView):
    """
    Should contain fieds 'avatar' with an image, 'user' with user pk
    """
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        up = UserProfile.objects.get(user__pk=request.data['user'])
        data = request.data
        del data['user']
        avatar_serializer = UserProfileAvatarSerializer(data=data, instance=up)
        if avatar_serializer.is_valid():
            avatar_serializer.save()
            return Response(avatar_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(avatar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def write_user_info(request):
    """
    Write user info. Shoud have header 'user' with pk of user instance, other fields you can see below:<br>
    <b>Sample</b>:<br>
    {"name": "fedor",<br>
    "vorname": "kondratenko",<br>
    "fathername": "igorevich",<br>
    "gender": 0,<br>
    "age": "2000-01-01",<br>
    "exp": 0,<br>
    "isFull": false,<br>
    "timeshift": 1,<br>
    "city": "SPb",<br>
    "send_push": true,<br>
    "user": 2,<br>
    "parkinson": "2000-01-01"}<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        up = UserProfile.objects.get(user__pk=request.data['user'])
        data = request.data
        del data['user']
        serializer = UserProfileSerializer(data=data, instance=up)
        if serializer.is_valid():
            serializer.save()
            up.isFull = True
            up.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def set_user_flags(request):
    """
    Sets different user flags. Shoud have header 'user' with pk of user instance and name of flag:<br>
    <b>List of flags:</b>
    1. isFull<br>
    2. isSurvey0<br>
    3. isSurvey1<br>
    4. isSurvey2<br>
    5. isPills<br>
    <b>Sample</b>:<br>
    {"user": 4,<br>
    "isFull": ""}<br>
    :param request:
    :return:
    """
    if request.method == 'POST':
        up = UserProfile.objects.get(user__pk=request.data['user'])
        if 'isFull' in request.data:
            up.isFull = True
            up.save()
            return Response({"message": "updated"})
        elif 'isSurvey0' in request.data:
            up.isSurvey0 = True
            up.save()
            return Response({"message": "updated"})
        elif 'isSurvey1' in request.data:
            up.isSurvey1 = True
            up.save()
            return Response({"message": "updated"})
        elif 'isSurvey2' in request.data:
            up.isSurvey2 = True
            up.save()
            return Response({"message": "updated"})
        elif 'isPills' in request.data:
            up.isPills = True
            up.save()
            return Response({"message": "updated"})
        elif 'isSick' in request.data:
            up.isSick = True
            up.save()
            return Response({"message": "updated"})
        else:
            return Response({"message": "error"})
    else:
        return Response({"message": "Method not allowed!"})


@api_view(['POST'])
def create_steps(request):
    """
    Counts steps per day.<br>
    <b>Sample</b><br>
    {"user": 5,<br>
    "steps": 1000}<br>
    :param request:
    :return:
    """
    day = datetime.datetime.now()
    try:
        steps_o = StepsCounter.objects.get_or_create(day=day,
                                                     user=User.objects.get(pk=request.data['user']))
        steps_o[0].steps = request.data['steps']
        steps_o[0].save()
        return Response({"message": "ok"})
    except:
        return Response({"errors": "error"})


@api_view(['POST'])
def get_steps(request):
    """
    Returns all steps for user.<br>
    <b>Sample</b><br>
    {"user": 5}<br>
    :param request:
    :return:
    """
    steps = StepsCounter.objects.filter(user=User.objects.get(pk=request.data['user'])).order_by('-day')
    serializer = StepsSerializer(steps, many=True)
    return Response({"steps": serializer.data})


@api_view(['POST'])
def get_depression(request):
    """
    Returns all depression recordings for user.<br>
    <b>Sample</b><br>
    {"user": 5}<br>
    :param request:
    :return:
    """
    steps = HADS_Result.objects.filter(user=User.objects.get(pk=request.data['user'])).order_by('-day')
    serializer = HADSSerializer(steps, many=True)
    return Response({"depression": serializer.data})


@api_view(['POST'])
def get_alarm(request):
    """
    Returns all depression recordings for user.<br>
    <b>Sample</b><br>
    {"user": 5}<br>
    :param request:
    :return:
    """
    steps = HADS_Alarm.objects.filter(user=User.objects.get(pk=request.data['user'])).order_by('-day')
    serializer = ALARMSerializer(steps, many=True)
    return Response({"alarm": serializer.data})


@api_view(['POST'])
def get_smiles(request):
    """
    Returns all smle test recordings for user.<br>
    <b>Sample</b><br>
    {"user": 5}<br>
    :param request:
    :return:
    """
    steps = SmileStats.objects.filter(user=User.objects.get(pk=request.data['user'])).order_by('-day')
    serializer = SmileSerializer(steps, many=True)
    return Response({"alarm": serializer.data})


@api_view(['POST'])
def search_user(request):
    data_s = str(request.data['text'])
    context = {'email': [],
               'username': [],
               'name': [],
               'fathername': [],
               'vorname': []}
    for word in data_s.split():
        context_e = UserProfile.objects.filter(user__email__icontains=word)
        context_u = UserProfile.objects.filter(user__username__icontains=word)
        context_n = UserProfile.objects.filter(name__icontains=word)
        context_f = UserProfile.objects.filter(fathername__icontains=word)
        context_v = UserProfile.objects.filter(vorname__icontains=word)
        context['name'].append(UserProfileAPISerializer(context_n, many=True).data)
        context['vorname'].append(UserProfileAPISerializer(context_v, many=True).data)
        context['fathername'].append(UserProfileAPISerializer(context_f, many=True).data)
        context['username'].append(UserProfileAPISerializer(context_u, many=True).data)
        context['email'].append(UserProfileAPISerializer(context_e, many=True).data)
    return Response(context)


@api_view(['POST'])
def connect_patient_to_arzt(request):
    """
    Connects patient to doctor. Should have header `user` with doctor id and header `pincode`<br>
    with patients pincode.<br>
    <b>Sample:</b><br>
    {"user": 44,<br>
    "pincode": "43DA82"}<br>
    :param request:
    :return:
    """
    try:
        user = User.objects.get(pk=request.data['user'])
    except:
        return Response({"message": "User not found"})
    try:
        patient = UserProfile.objects.get(pincode=request.data['pincode'])
    except:
        return Response({"message": "Patient with this pincode not found"})
    patient.doctor = user
    patient.save()
    return Response({"message": "ok"})


@api_view(['POST'])
def get_current_doctor(request):
    """
    Get info about doctor<br>
    <b>Sample:</b><br>
    {"user": 44}<br>
    :param request:
    :return:
    """
    try:
        user = User.objects.get(pk=request.data['user'])
    except:
        return Response({"message": "User not found"})
    up = UserProfile.objects.get(user=user)
    return Response({"doctor": UserProfileAPISerializer(up).data})
