from videos.models import Video, CategoriaVideo
from videos.serializers import VideoSerializer, CategoriaSerializer
from rest_framework import viewsets, generics, filters
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

'''@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
'''



class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo']
    permission_classes = [IsAuthenticated]

class VideoFreeViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()[0:5]
    serializer_class = VideoSerializer
    http_method_names = ['get']





class CategoriaViewSet(viewsets.ModelViewSet):

    queryset = CategoriaVideo.objects.all()
    serializer_class = CategoriaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']
    permission_classes = [IsAuthenticated]

class VideoCategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    def get_queryset(self):
        id_categoria = self.kwargs['id_categoria']
        return Video.objects.filter(categoriaId=id_categoria)


