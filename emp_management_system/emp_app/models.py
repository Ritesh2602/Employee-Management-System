from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100)

class Role(models.Model):
    name=models.CharField(max_length=100,null=False)

class Employee(models.Model):
    firstName=models.CharField(max_length=50,null=False)
    lastName=models.CharField(max_length=50,null=False)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)


