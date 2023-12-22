from rest_framework import serializers
from videos.models import Video, CategoriaVideo

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaVideo
        fields = '__all__'
