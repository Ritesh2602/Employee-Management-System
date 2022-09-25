from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def view_emp(request):
    return render(request, 'view_emp.html')

def add_emp(request):
    return render(request, 'add_emp.html')

def del_emp(request):
    return render(request,'del_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')

