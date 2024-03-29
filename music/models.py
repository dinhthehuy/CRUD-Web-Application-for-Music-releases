import uuid

from django.db import models


# Create your models here.

class Artist(models.Model):
    mbid = models.CharField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name


class Album(models.Model):
    mbid = models.CharField(primary_key=True)
    name = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    num_songs = models.IntegerField(null=True, blank=True)
    image_url = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name


class Log(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True, default=None)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True, default=None)
    logged_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.logged_date} {self.album.name} - {self.artist.name}"


class AlbumTag(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField()
    count = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('album', 'name', 'count')

    def __str__(self):
        return self.name

