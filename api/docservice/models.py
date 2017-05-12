from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField()

class ImageDocument(models.Model):
    name = models.CharField(max_length=50)
    image = FileField()

class ImageType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    imagedoc = models.ForeignKey('ImageDocument', on_delete=SET_NULL)

class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    createdDate = models.DateTimeField()
    modifiedDate = models.DateTimeField()
