from django.shortcuts import render
from videos.models import Video, CategoriaVideo
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from videos.serializers import VideoSerializer, CategoriaSerializer
from django.core import serializers
from rest_framework import viewsets, generics, filters

# Create your views here.

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo']

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = CategoriaVideo.objects.all()
    serializer_class = CategoriaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

class VideoCategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    def get_queryset(self):
        id_categoria = self.kwargs['id_categoria']
        return Video.objects.filter(categoriaId=id_categoria)

