import time

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import SurveyShedule, MessageSurvey


@api_view(['POST'])
def reload_all_shedules(request):
    print("start reloading")
    ss_o = SurveyShedule.objects.all()
    for obj in ss_o:
        time.sleep(0.2)
        obj.save()
    ss_o = MessageSurvey.objects.all()
    for obj in ss_o:
        time.sleep(0.2)
        obj.save()
    print("reloading completed")
    return Response({"message": "reloaded"})
