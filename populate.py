import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

import random

from faker import Faker

from videos.models import InfoVideos, CategoriaVideos

def criando_videos(quantidade_videos):
    fake = Faker('pt-BR')
    Faker.seed(1)
    for _ in range(quantidade_videos):
        titulo = fake.sentence(nb_words=10, variable_nb_words=False)
        descricao = fake.sentence(nb_words=10)
        url = fake.sentence(nb_words=10)
        categoriaId = "{}".format(random.randrange(1, 5))
        v = InfoVideos(titulo=titulo,descricao=descricao,url=url,categoriaId=categoriaId)
        v.save()
def criando_categorias(quantidade_categorias):
    fake = Faker('pt-BR')
    for _ in range(quantidade_categorias):
        titulo = fake.sentence(nb_words=3)
        cor = fake.safe_color_name()
        c = CategoriaVideos(titulo=titulo,cor=cor)
        c.save()

criando_categorias(5)
criando_videos(2)