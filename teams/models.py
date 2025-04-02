from django.db import models

# Create your models here.

class Teams(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=75)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary