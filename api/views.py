from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters

from .serializers import VideoSerializer
from .models import Video


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('published_at')
    serializer_class = VideoSerializer

class SearchAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all().order_by('published_at')
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)
    serializer_class = VideoSerializer