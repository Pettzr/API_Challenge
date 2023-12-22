from videos.serializers import VideoSerializer, CategoriaSerializer
from videos.models import Video, CategoriaVideo
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

class SerializerVideoTestCase(APITestCase):

    def setUp(self):
        self.video = Video.objects.create(titulo='djangotest1', descricao='djangotest1',
                                            url='djangotest1', categoriaId='9')
        self.serializer = VideoSerializer(instance=self.video)

    def test_video_serializer_itens(self):
        data = self.serializer.data
        self.assertEquals(set(data.keys()), set(['id','titulo', 'descricao', 'url', 'categoriaId']))

    def test_video_serializer_conteudo(self):
        data = self.serializer.data
        self.assertEquals(data['id'], self.video.id)
        self.assertEquals(data['titulo'], self.video.titulo)
        self.assertEquals(data['descricao'], self.video.descricao)
        self.assertEquals(data['url'], self.video.url)
        self.assertEquals(data['categoriaId'], self.video.categoriaId)

class SerializerCategoriaTestCase(APITestCase):

    def setUp(self):
        self.categoria= CategoriaVideo.objects.create(titulo='djangotest1', cor='azul')
        self.serializer = CategoriaSerializer(instance=self.categoria)

    def test_categoria_serializer_itens(self):
        data = self.serializer.data
        self.assertEquals(set(data.keys()), set(['id','titulo', 'cor']))

    def test_video_serializer_conteudo(self):
        data = self.serializer.data
        self.assertEquals(data['id'], self.categoria.id)
        self.assertEquals(data['titulo'], self.categoria.titulo)
        self.assertEquals(data['cor'], self.categoria.cor)

