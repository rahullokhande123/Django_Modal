from django.shortcuts import render
from django.http import HttpResponse
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
                use_name=Student.objects.filter(stu_name=name)
                if use_name:
                    msg="Email ID and Name already exist"
                    return render(request, 'register.html',{'msg':msg})
                else:
                    msg="Email id already exist please choose other 'email ID'"
                    return render(request, 'register.html',{'msg':msg})
            else:
                Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
                msg="YOUR DATA SUCCESSFULLY RECORDED"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Password not match"
            return render (request,"register.html",{'msg':msg})

    #=======================================================================================================   
        # user=Student.objects.get(stu_email=email)
        # Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
        # msg="DATA SUCCESSFULLY SUBMITED"
        # return render(request,'home.html',{'msg':msg})
    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)
        use=Student.objects.filter(stu_email=email)
        print(use)
        if use:
            use_data=Student.objects.get(stu_email=email)
            print(use_data)
            email1=use_data.stu_email
            name1=use_data.stu_name
            contact1=use_data.stu_contact 
            password1=use_data.stu_password
            print(email1,name1,contact1,password1)
            if password1==password:
                data={
                    'nm':name1,
                    'em':email1,
                    'con':contact1,
                    'pas':password1
                }
                return render(request,'dashboard.html',data)
            else:
                msg="You Entered Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Email Id not Register"
            return render(request,'login.html',{'msg':msg})        
    else:
        return render(request,'login.html')
    
def first(requst):
    data=Student.objects.first()
    print(data)
    print(data.id,data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
    my_data={
        'nm':data.stu_name,
        'em':data.stu_email,
        'con':data.stu_contact,
        'pas':data.stu_password
    }
    return render (requst,'dashboard.html',my_data)

def last(request):
    data=Student.objects.last()
    print(data)
    print(data.id,data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
    my_data={
        'nm':data.stu_name,
        'em':data.stu_email,
        'con':data.stu_contact,
        'pas':data.stu_password
    }
    return render (request,'dashboard.html',my_data)

def letest(request):
    data=Student.objects.latest("id")
    print(data)
    print(data.id,data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
    my_data={
        'nm':data.stu_name,
        'em':data.stu_email,
        'con':data.stu_contact,
        'pas':data.stu_password
    }
    return render (request,'dashboard.html',my_data)

def earliast(request):
    data=Student.objects.earliest("id")
    print(data)
    print(data.id,data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
    my_data={
        'nm':data.stu_name,
        'em':data.stu_email,
        'con':data.stu_contact,
        'pas':data.stu_password
    }
    return render (request,'dashboard.html',my_data)

def exists(request):
    data = Student.objects.all()
    print(data.exists())
    return HttpResponse(data)


def create(request):
    data = Student.objects.create(stu_name='Ramkumar',stu_email='ramkumar@gmail.com',stu_contact=852741963,stu_password=789)
    print(data.id, data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
    my_data={
        'nm':data.stu_name,
        'em':data.stu_email,
        'con':data.stu_contact,
        'pas':data.stu_password
    }
    return render (request,'dashboard.html',my_data)




