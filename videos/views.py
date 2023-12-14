from django.shortcuts import render
from videos.models import InfoVideos
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from videos.serializers import VideoSerializer
from django.core import serializers
from rest_framework import viewsets, generics

# Create your views here.

class VideoViewSet(viewsets.ModelViewSet):
    queryset = InfoVideos.objects.all()
    serializer_class = VideoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

def videoID(request, post_id):
    video = serializers.serialize('json', InfoVideos.objects.filter_by('id'))

