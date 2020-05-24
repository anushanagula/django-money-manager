from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import addIncomeForm,addExpenseForm
from .models import Income,Expense
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from itertools import chain
import operator

def home(request):
    return render(request, 'wallet/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'wallet/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('mywallet')
            except IntegrityError:
                return render(request, 'wallet/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'wallet/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'wallet/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'wallet/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('mywallet')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def addincome(request):
    if request.method == 'GET':
        return render(request, 'wallet/addincome.html', {'form':addIncomeForm()})
    else:
        try:
            form = addIncomeForm(request.POST)
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('mywallet')
        except ValueError:
            return render(request, 'wallet/addincome.html', {'form':addIncomeForm(), 'error':'Bad data passed in. Try again.'})
@login_required 
def addexpense(request):
    if request.method == 'GET':
        return render(request, 'wallet/addexpense.html', {'form':addExpenseForm()})
    else:
        try:
            form = addExpenseForm(request.POST)
            expense= form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('mywallet')
        except ValueError:
            return render(request, 'wallet/addexpense.html', {'form':addExpenseForm(), 'error':'Bad data passed in. Try again.'})



@login_required
def mywallet(request):
    income = Income.objects.filter(user=request.user).aggregate(Sum('amount'))
    income=income['amount__sum']
    expense = Expense.objects.filter(user=request.user).aggregate(Sum('amount'))
    expense=expense['amount__sum']
    if not income:
        income=0 
    if not expense:
        expense=0
    return render(request, 'wallet/mywallet.html', {'income':income,'expense':expense,'balance':income-expense})

@login_required
def viewincome(request, income_pk):
    income = get_object_or_404(Income, pk=income_pk, user=request.user)
    if request.method == 'GET':
        form = addIncomeForm(instance=income)
        return render(request, 'wallet/viewincome.html', {'income':income, 'form':form})
    else:
        try:
            form = addIncomeForm(request.POST, instance=income)
            form.save()
            return redirect('mywallet')
        except ValueError:
            return render(request, 'wallet/viewincome.html', {'income':income, 'form':form, 'error':'Bad info'})
@login_required
def viewexpense(request, expense_pk):
    expense = get_object_or_404(Expense, pk=expense_pk, user=request.user)
    if request.method == 'GET':
        form = addExpenseForm(instance=expense)
        return render(request, 'wallet/viewexpense.html', {'expense':expense, 'form':form})
    else:
        try:
            form = addExpenseForm(request.POST, instance=expense)
            form.save()
            return redirect('mywallet')
        except ValueError:
            return render(request, 'wallet/viewexpense.html', {'expense':expense, 'form':form, 'error':'Bad info'})

@login_required
def transaction(request):
    income = Income.objects.filter(user=request.user)
    expense = Expense.objects.filter(user=request.user)
    transactions=chain(income,expense)
    transactions = sorted(transactions, key=operator.attrgetter('date'),reverse=True)
    return render(request,'wallet/transactions.html',{'expense':expense,'income':income,'transactions':transactions})

@login_required
def deleteexpense(request, expense_pk):
    expense = get_object_or_404(Expense, pk=expense_pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('mywallet')
@login_required
def deleteincome(request,income_pk):
    income= get_object_or_404(Income, pk=income_pk, user=request.user)
    if request.method == 'POST':
        income.delete()
        return redirect('mywallet')