from django.db import models
from datetime import datetime
from chefs.models import Chef



class Menu(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title

