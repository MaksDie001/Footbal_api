from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import *
from .serializer import TeamSerializer, MatcSerializer

class TeamRetrieveAPIView(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class MatcListAPIView(ListAPIView):
    queryset = Matc.objects.all()
    serializer_class = MatcSerializer