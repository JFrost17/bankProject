from django.db import models
from decimal import Decimal
from django.conf import settings

# Create your models here.

class Deposit(models.Model):
    depositAmount = models.DecimalField(decimal_places=2, max_digits=65)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "${}".format(self.depositAmount)

class Withdrawl(models.Model):
    withdrawlAmount = models.DecimalField(decimal_places=2, max_digits=65)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default="")

    def __str__(self):
        return "${}".format(self.withdrawlAmount)