from django.db import models

# Create your models here.

class Deposit(models.Model):
    depositAmount = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.depositAmount

class Withdrawl(models.Model):
    withdrawlAmount = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.withdrawlAmount