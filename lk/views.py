from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import UserProfileForm
from .models import UserProfile, DiaryRecording, NewsRecording
from .serializers import DiaryRecordingSerializer, NewsRecordingSerializer, \
    UserProfileSerializer, UserProfileAPISerializer


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


@login_required()
@api_view(['GET', 'POST'])
def get_diary_list(request):
    """
    Creates new diary recording or returns all recording list
    :param request:
    :return:
    """
    if request.method == 'GET':
        return Response({"recordings": DiaryRecordingSerializer(DiaryRecording.objects.filter(user=request.user),
                                                                many=True).data})
    elif request.method == 'POST':
        serializer = DiaryRecordingSerializer(data=request.data)
        try:
            DiaryRecording.objects.create(user=request.user, header=request.data['header'],
                                          text=request.data['text'])
            return Response({"message": "Recording created!"})
        except KeyError:
            return Response({"message": "Error!"})
    else:
        return Response({"message": "Method not allowed!"})


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


@api_view(['GET', 'POST'])
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
