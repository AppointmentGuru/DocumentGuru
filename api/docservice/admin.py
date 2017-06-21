from __future__ import unicode_literals

from django.contrib import admin
from .models import Document, ImageDocument, ImageType, Note

# Register your models here.
admin.site.register(Document)
admin.site.register(ImageDocument)
admin.site.register(ImageType)
admin.site.register(Note)
