from django.shortcuts import render
from home import models
from .models import homes
# Create your views here.

def home(request):
    if request.method == "POST":
        expenseName = request.POST['expenseName']
        expenseAmount = request.POST['expenseAmount']
        date = request.POST['date']
        ins = models.homes(expenseName = expenseName, expenseAmount = expenseAmount, date=date)
        ins.save()
        print("Data Posted to DB") #Used for debugging
    return render(request,'registration.html')

def table(request):
    formData = homes.objects.all()
    data = {
        'formData': formData
    }
    return render(request,'table.html',data)
