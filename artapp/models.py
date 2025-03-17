from django.db import models

# Create your models here.

class Booking(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=15)
    datetime=models.DateTimeField()
    message=models.TextField()

    def __str__(self):
        return self.name
