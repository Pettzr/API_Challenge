from rest_framework import serializers
from videos.models import InfoVideos

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoVideos
        fields = '__all__'
