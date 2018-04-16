"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=40)

class Song(models.Model):
    title = models.CharField(max_length=40)
    artist = models.ManyToManyField(Artist)