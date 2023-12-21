from typing import Any
from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    type = models.CharField(max_length=100)
    lifespan = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return f'{self.type} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

