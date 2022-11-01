from django.db import models

# Create your models here.
class Post(models.Model):
    item = models.CharField(max_length=50)
    itemIndex = models.IntegerField()
    spotX = models.FloatField()
    spotY = models.FloatField()
    budget = models.IntegerField()
    # spotX and spotY is for google api spot
    def __str__(self):
        return f'[{self.pk}]{self.item}'
