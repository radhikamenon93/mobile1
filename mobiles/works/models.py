from django.db import models
class Mobile(models.Model):
    brand=models.CharField(max_length=20)
    price=models.PositiveIntegerField()
    year=models.PositiveIntegerField()
    color=models.CharField(max_length=20)

# Create your models here.
