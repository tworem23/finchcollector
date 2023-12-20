from django.db import models

# Create your models here.
class Finch(models.Model):
    type = models.CharField(max_length=100)
    lifespan = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return f'{self.type} ({self.id})'

