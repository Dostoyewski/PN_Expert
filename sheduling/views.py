from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import SurveyShedule, MessageSurvey


@api_view(['POST'])
def reload_all_shedules(request):
    ss_o = SurveyShedule.objects.all()
    for obj in ss_o:
        obj.save()
    ss_o = MessageSurvey.objects.all()
    for obj in ss_o:
        obj.save()
    return Response({"message": "reloaded"})
