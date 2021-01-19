from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse

from lk.models import UserProfile
from .forms import CompetitionRecordingForm
from .models import Competition, CompetitionRecording
from .serializers import CompetitionSerializer


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


def grishas_intro(request):
    """
    intro for smartphones
    :param request:
    :return:
    """
    return render(request, 'grishas-intro.html', {})


def grishas_intro_timer(request):
    """
    intro for smartphones
    :param request:
    :return:
    """
    return render(request, 'grishas-timer.html', {})


def competitions_list(request):
    """
    Page with all competitions tasks
    :param request:
    :return:
    """
    competitions = Competition.objects.all()
    # Array with serialized competitions
    comp_arr = []
    if not request.user.is_anonymous:
        for obj in competitions:
            serialized = CompetitionSerializer(obj).data
            try:
                rec = get_list_or_404(CompetitionRecording, user=request.user, competition=obj)
                serialized['ifExist'] = True
            except:
                serialized['ifExist'] = False
            comp_arr.append(serialized)
        return render(request, 'videos_home.html', {"recordings": comp_arr,
                                                    "message": "ok"})
    else:
        return render(request, 'videos_home.html', {"recordings": CompetitionSerializer(Competition.objects.all(),
                                                                                        many=True).data,
                                                    "message": "Для загрузки видео необходимо войти"})
