from django.db import models
# Create your models here.
class Song(models.Model):
    music_name = models.CharField(max_length=150)
    artiste = models.CharField(max_length=200)
    music_file = models.FileField(upload_to='media/music')
    cover_image = models.ImageField(upload_to='media/images')
    time_length = models.IntegerField()