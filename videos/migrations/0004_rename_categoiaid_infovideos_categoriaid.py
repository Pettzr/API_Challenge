# Generated by Django 5.0 on 2023-12-16 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_infovideos_categoiaid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infovideos',
            old_name='categoiaId',
            new_name='categoriaId',
        ),
    ]
