# Generated by Django 2.0.5 on 2018-05-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
