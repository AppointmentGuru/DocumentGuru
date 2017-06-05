from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField()

class ImageDocument(models.Model):
    name = models.CharField(max_length=50)
    upload = models.FileField(upload_to='uploads/')

class ImageType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    imageDoc = models.ForeignKey('ImageDocument', null=True, blank=True, on_delete=models.SET_NULL)

class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    createdDate = models.DateTimeField()
    modifiedDate = models.DateTimeField()
    images = models.ForeignKey('ImageDocument', null=True, blank=True, on_delete=models.SET_NULL)
    documents = models.ForeignKey('Document', null=True, blank=True, on_delete=models.SET_NULL)
