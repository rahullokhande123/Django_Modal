from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            user=Student.objects.filter(stu_email=email)
            print(user)
            if user:
               msg="Data Alrady Exist"
               return render(request,'register.html',{'msg':msg})
            else:
              Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
              msg="DATA SUCCESSFULLY SUBMITED"
              return render(request,'login.html',{'msg':msg})
        else:
            msg="Password not match"
            return render (request,"register.html",{'msg':msg})

        
        # user=Student.objects.get(stu_email=email)
        

        # Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
        # msg="DATA SUCCESSFULLY SUBMITED"
        # return render(request,'home.html',{'msg':msg})
    else:
        return render(request,'register.html')

def login(request):
    return render(request,'login.html')