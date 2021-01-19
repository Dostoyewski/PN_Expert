from django import forms

from .models import CompetitionRecording


class CompetitionRecordingForm(forms.ModelForm):
    class Meta:
        model = CompetitionRecording
        fields = ['video']

    def clean_video(self):
        video = self.cleaned_data['video']

        try:
            # validate content type
            main, sub = video.content_type.split('/')
            if not (main == 'video' and sub in ['avi', 'mp4']):
                raise forms.ValidationError(u'Разрешенные форматы — .avi или .mp4. Пожалуйста,'
                                            u' загрузите видео разрешенного формата.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass
        return video
