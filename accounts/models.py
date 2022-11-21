from django.db import models


# Create your models here.
class IceCream(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    email=models.EmailField()
    name=models.CharField(max_length=50)
    date=models.DateField()

    def __str__(self):
        return self.title