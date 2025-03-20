from django.db import models

# Create your models here.

class hiring(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=15)
    datetime=models.DateTimeField()
    message=models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=15)
    datetime=models.DateTimeField()
    message=models.TextField()

    def __str__(self):
        return self.name

#Mpesa Api
#new


class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"


