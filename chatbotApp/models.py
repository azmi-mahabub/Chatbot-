from django.db import models
from django.contrib.auth.models import User

class Piece(models.Model):
    reference = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    volume = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    keywords = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.reference} - {self.designation}"

