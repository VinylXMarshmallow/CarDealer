# cars/models.py
from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=250, blank=False, unique=False)
    content = models.TextField(default='')
    year = models.PositiveSmallIntegerField(default=2023)
    imgThumb = models.ImageField(upload_to="media_img", null=True, blank=True)
   
    def __str__(self):
        return f"{self.year} {self.title}"
