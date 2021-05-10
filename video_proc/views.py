from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lk.models import UserProfile
from .forms import CompetitionRecordingForm
from .models import Competition, CompetitionRecording
from .serializers import CompetitionSerializer, CompetitionRecordingSerializer


@login_required()
def video_recording(request, slug):
    """
    This function return video page
    :param request:
    :param slug: slug to UProfile
    :return: render
    """
    v_profile = get_object_or_404(Competition, slug=slug)
    if request.method == 'POST':
        form = CompetitionRecordingForm(request.POST, request.FILES)
        if form.is_valid():
            recording = CompetitionRecording()
            recording.video = form.cleaned_data['video']
            recording.user = request.user
            recording.competition = v_profile
            recording.save()
            u_profile = UserProfile.objects.get(user=request.user)
            u_profile.exp += v_profile.exp
            u_profile.save()
            return HttpResponseRedirect(reverse('competition_list'))
    else:
        try:
            recording = get_object_or_404(CompetitionRecording, user=request.user, competition=v_profile)
            has_loaded = True
        except:
            has_loaded = False
            recording = ''
        form = CompetitionRecordingForm()
        return render(request, 'competition_detail.html', {'comp_profile': v_profile,
                                                           'form': form,
                                                           'absolute': reverse('video_rec', args=(v_profile.slug,)),
                                                           'result': recording,
                                                           'hasLoaded': has_loaded})


@api_view(['GET', 'POST'])
def competition_list(request):
    """
    Returns list of competitions or concrete competition.
    <b>Sample:</b><br>
    {"competition": 1}
    :param request:
    :return:
    """
    if request.method == 'GET':
        objs = Competition.objects.all()
        return Response({"competitions": CompetitionSerializer(objs, many=True).data})
    elif request.method == 'POST':
        obj = Competition.objects.get(pk=request.data['competition'])
        return Response({"competitions": CompetitionSerializer(obj).data})


@api_view(['POST'])
def create_recording(request):
    """
    Should contain fields 'user', 'video', 'competition'
    :param request:
    :return:
    """
    serializer = CompetitionRecordingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "ok"})
    else:
        return Response({"error": serializer.errors})
