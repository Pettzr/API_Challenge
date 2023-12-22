from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from videos.models import Video, CategoriaVideo
from rest_framework import status



# Create your tests here.

class VideoTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Video-list')
        self.video1 = Video.objects.create(titulo='djangotest1', descricao='djangotest1',
                                            url='djangotest1', categoriaId='9')
        self.video2 = Video.objects.create(titulo='djangotest2', descricao='djangotest2',
                                            url='djangotest2', categoriaId='9')

    def test_get_listar_video(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_video(self):
        response = self.client.delete('/videos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_video(self):
        data = {
            'titulo' : 'titulo put',
            'descricao' : 'aaaa',
            'url': 'url',
            'categoriaId': '2'
        }
        response = self.client.put('/videos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_video(self):
        data = {
            'titulo' : 'titulo post',
            'descricao' : 'aaaa',
            'url': 'url',
            'categoriaId': '2'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


class CategoriaTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Categoria-list')
        self.categoria1 = CategoriaVideo.objects.create(id='3', titulo='djangotestcategoria1', cor='test1')
        self.categoria2 = CategoriaVideo.objects.create(titulo='djangotestcategoria2', cor='test2')

    def test_get_listar_categoria(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_categoria(self):
        response = self.client.delete('/categorias/4/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_categoria(self):
        data = {
            'titulo': 'title put',
            'cor': 'test'
        }
        response = self.client.put('/categorias/3/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_categoria(self):
        data = {
            'titulo': 'titulo post',
            'cor': 'test'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

class CategoriaVideoTestCase(APITestCase):

    def setUp(self):
        self.categoria1 = CategoriaVideo.objects.create(titulo='djangotestcategoria1', cor='test1')
        self.categoria2 = CategoriaVideo.objects.create(titulo='djangotestcategoria2', cor='test2')
        self.video1 = Video.objects.create(titulo='djangotest1', descricao='djangotest1',
                                                url='djangotest1', categoriaId='1')
        self.video2 = Video.objects.create(titulo='djangotest2', descricao='djangotest2',
                                                url='djangotest2', categoriaId='1')
        self.video3 = Video.objects.create(titulo='djangotest3', descricao='djangotest3',
                                                url='djangotest3', categoriaId='2')

    def test_get_categoria_1_video(self):
        response_video1 = self.client.get('/categorias/1/videos/1/')
        response_video2 = self.client.get('/categorias/1/videos/2/')
        self.assertEquals(response_video1.status_code, status.HTTP_200_OK)
        self.assertEquals(response_video2.status_code, status.HTTP_200_OK)

    def test_get_categoria_2_video(self):
        response_video1 = self.client.get('/categorias/2/videos/3/')
        response_video2 = self.client.get('/categorias/2/videos/1/')
        self.assertEquals(response_video1.status_code, status.HTTP_200_OK)
        self.assertEquals(response_video2.status_code, status.HTTP_404_NOT_FOUND)
