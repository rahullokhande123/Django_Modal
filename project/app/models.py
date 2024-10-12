from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_password=models.CharField(max_length=25)
    stu_image = models.ImageField(upload_to='image/')
    stu_resume = models.FileField(upload_to='file/')

    def __str__(self):
       return self.stu_name
class Query(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    query=models.TextField()

    def __str__(self):
        return self.query