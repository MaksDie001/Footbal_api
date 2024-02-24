from rest_framework import serializers
from .models import Team, Matc

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class MatcSerializer(serializers.ModelSerializer):
    first_team = TeamSerializer()
    second_team = TeamSerializer()

    class Meta:
        model = Matc
        fields = "__all__"