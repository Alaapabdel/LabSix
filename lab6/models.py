from django.db import models

# Create your models here.
class BankAccount(models.Model):
    credit_card= models.CharField(max_length=19)
    pin= models.IntegerField()

class Feedback(models.Model):
    message = models.CharField(max_length=100)
    nationalID = models.FileField(null = True, blank = True)

class Branch(models.Model):
    country= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    street= models.CharField(max_length=100)