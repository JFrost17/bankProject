from django import forms
from django.forms import ModelForm
from .models import *
from django.http import *

class DepositForm(forms.ModelForm):
        class Meta:
            model = Deposit
            exclude = ["user"]
        def clean_depositAmount(self):
            depositAmount = self.cleaned_data.get("depositAmount")
            if(depositAmount <= 0):
                raise forms.ValidationError("Deposit amount must be greater than 0.")
            return depositAmount

class WithdrawlForm(forms.ModelForm):
    class Meta:
        model = Withdrawl
        exclude = ["user"]
    def clean_withdrawlAmount(self):
        withdrawlAmount = self.cleaned_data.get("withdrawlAmount")
        if(withdrawlAmount <= 0):
            raise forms.ValidationError("Withdrawl amount must be greater than 0.")
        return withdrawlAmount

