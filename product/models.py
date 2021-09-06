from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=120)
    # is_active = models.BooleanField(default=True)


class Album(models.Model):
    title = models.CharField(max_length=160)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)


class MediaType(models.Model):
    name = models.CharField(max_length=120)


class Genre(models.Model):
    name = models.CharField(max_length=120)


class Track(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    mediatype = models.ForeignKey(MediaType, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    composer = models.CharField(max_length=200, blank=True, null=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unit_price = models.IntegerField()
