from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import VideoSerializer
from .models import Video


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('published_at')
    serializer_class = VideoSerializer