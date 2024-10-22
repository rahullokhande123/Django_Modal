from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_password=models.CharField(max_length=25)

    def __str__(self):
       return self.stu_name
class Query(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    query=models.TextField()

    def __str__(self):
        return self.query
    

class Aadhar(models.Model):
    aadhar=models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.aadhar)
    
class Department(models.Model):
    dep_name=models.CharField(max_length=50)
    dep_des=models.TextField()
    def __str__(self):
        return str(self.dep_name)


class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    aadhar_no=models.OneToOneField(Aadhar,on_delete=models.CASCADE)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)