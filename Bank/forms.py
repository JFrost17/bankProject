from django import forms
from django.forms import ModelForm
from .models import *

class DepositForm(forms.ModelForm):
        class Meta:
            model = Deposit
            fields = '__all__'

class WithdrawlForm(forms.ModelForm):
    class Meta:
        model = Withdrawl
        fields = '__all__'