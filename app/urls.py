from django.urls import path
from .views import *
urlpatterns = [
    path("",MatcListAPIView.as_view()),
    path('teams/<int:pk>/', TeamRetrieveAPIView.as_view(), name='team-detail'),
]
