from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    deposits = Deposit.objects.all()
    withdrawls = Withdrawl.objects.all()
    accountBalance = 0
    for deposit in deposits:
        accountBalance += int(deposit.depositAmount)
    for withdrawl in withdrawls:
        accountBalance -= int(withdrawl.withdrawlAmount)
    form = DepositForm()
    formTwo = WithdrawlForm()
    if request.method == 'POST':
        form = DepositForm(request.POST)
        formTwo = WithdrawlForm(request.POST)
        if form.is_valid():
            form.save()
        if formTwo.is_valid():
            formTwo.save()
        return redirect('/')
    accountString ="Account Balance: $"+str(accountBalance)
    return render(request, 'Bank/list.html',{'deposits':deposits,'withdrawls':withdrawls,'accountString':accountString,'form':form,'formTwo':formTwo})