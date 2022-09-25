from django.shortcuts import render
from .models import Department,Role,Employee

# Create your views here.
def index(request):
    return render(request, 'index.html')

def view_emp(request):
    emp=Employee.objects.all()
    params={
        'emps':emp
    }
    print(params)
    return render(request, 'view_emp.html',params)

def add_emp(request):
    return render(request, 'add_emp.html')

def del_emp(request):
    return render(request,'del_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')

