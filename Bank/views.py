from decimal import Decimal
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

@login_required(login_url='login')
def index(request):
    currentUser = request.user.username
    deposits = Deposit.objects.all()
    withdrawls = Withdrawl.objects.all()
    accountBalance = Decimal(0.00)
    for deposit in deposits:
        if deposit.user == request.user:
            accountBalance = accountBalance + Decimal(deposit.depositAmount)
    for withdrawl in withdrawls:
        if withdrawl.user == request.user:
            accountBalance = accountBalance - Decimal(withdrawl.withdrawlAmount)
    form = DepositForm()
    formTwo = WithdrawlForm()
    if request.method == 'POST':
        if "withdrawlAmount" in request.POST:
            withdraw_form = WithdrawlForm({"withdrawlAmount": request.POST["withdrawlAmount"]})
            if withdraw_form.is_valid():
                withdraw_form.instance.user = request.user
                withdraw_form.save()

        if "depositAmount" in request.POST:
            deposit_form = DepositForm( {"depositAmount": request.POST["depositAmount"]})
            if deposit_form.is_valid():
                deposit_form.instance.user = request.user
                deposit_form.save()

        return redirect('/')
    return render(request, 'Bank/list.html',
                  {'deposits':deposits,'withdrawls':withdrawls,
                   'accountBalance':accountBalance,'form':form,'formTwo':formTwo,'request':request})

def register(request):
    if request.method == "GET":
        return render(
            request, "Bank/register.html",
            {"form": UserCreationForm}
        )
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
        else:
            return redirect('/register')
        return redirect('/login')
    return redirect('/register')
