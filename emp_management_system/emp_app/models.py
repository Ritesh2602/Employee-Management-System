from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    firstName=models.CharField(max_length=50,null=False)
    lastName=models.CharField(max_length=50)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)


    def __str__(self):
       return  "%s %s" %(self.firstName,self.lastName)


