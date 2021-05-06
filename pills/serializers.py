from rest_framework.serializers import ModelSerializer

from .models import Pill, AssignedPill


class PillSerializer(ModelSerializer):
    class Meta:
        model = Pill
        fields = "__all__"


class AssignedPillSerializer(ModelSerializer):
    class Meta:
        model = AssignedPill
        fields = '__all__'
