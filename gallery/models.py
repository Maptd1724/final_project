from django.db import models
from chefs.models import Chef

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title
