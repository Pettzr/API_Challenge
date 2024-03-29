"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.shortcuts import redirect
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new



from videos.views import VideoViewSet, VideoFreeViewSet, CategoriaViewSet, VideoCategoriaViewSet

router = routers.DefaultRouter()
router.register(r'videos/free', VideoFreeViewSet, basename='VideoFree')
router.register(r'videos', VideoViewSet, basename='Video')
router.register(r'categorias', CategoriaViewSet, basename='Categoria')
router.register('categorias/(?P<id_categoria>.+)/videos', VideoCategoriaViewSet, basename='categoria_video')



urlpatterns = [
    path('configs-admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns() # new
