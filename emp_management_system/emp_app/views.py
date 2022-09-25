from django.shortcuts import render,HttpResponse
from .models import Department,Role,Employee

# Create your views here.
def index(request):
    return render(request, 'index.html')

def view_emp(request):
    emp=Employee.objects.all()
    params={
        'emps':emp
    }
    return render(request, 'view_emp.html',params)

def add_emp(request):
     if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=request.POST['role']
        phone=int(request.POST['phone'])
        Dept = Department(name=dept)
        RoleEmp = Role(name=role)
        Dept.save()
        RoleEmp.save()
        employee=Employee(firstName=first_name,lastName=last_name,salary=salary,bonus=bonus,phone=phone,dept=Dept,role=RoleEmp)
        employee.save()
        return HttpResponse("Employee added successfully")

     elif request.method=='GET':
         return render(request,'add_emp.html')

     else:
         return HttpResponse("Connection error")

def del_emp(request):
    return render(request,'del_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')

