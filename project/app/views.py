from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import Query

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
                all_query=Query.objects.filter(email=email1)
                return render(request,'dashboard.html',{'key1':all_query,'data':data})
            else:
                msg="You Entered Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Email Id not Register"
            return render(request,'login.html',{'msg':msg})        
    else:
        return render(request,'login.html')

# ====================== Single Objects ======================= 
  
# def first(requst):
#     data=Student.objects.first()
#     print(data)
#     print(data.id,data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
#     my_data={
#         'nm':data.stu_name,
#         'em':data.stu_email,
#         'con':data.stu_contact,
#         'pas':data.stu_password
#     }
#     return render (requst,'dashboard.html',my_data)

# def last(request):
#     data=Student.objects.last()
#     print(data)
#     print(data.id,data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
#     my_data={
#         'nm':data.stu_name,
#         'em':data.stu_email,
#         'con':data.stu_contact,
#         'pas':data.stu_password
#     }
#     return render (request,'dashboard.html',my_data)

# def letest(request):
#     data=Student.objects.latest("id")
#     print(data)
#     print(data.id,data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
#     my_data={
#         'nm':data.stu_name,
#         'em':data.stu_email,
#         'con':data.stu_contact,
#         'pas':data.stu_password
#     }
#     return render (request,'dashboard.html',my_data)

# def earliast(request):
#     data=Student.objects.earliest("id")
#     print(data)
#     print(data.id,data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
#     my_data={
#         'nm':data.stu_name,
#         'em':data.stu_email,
#         'con':data.stu_contact,
#         'pas':data.stu_password
#     }
#     return render (request,'dashboard.html',my_data)

# def exists(request):
#     data = Student.objects.all()
#     print(data.exists())
#     return HttpResponse(data)


# def create(request):
#     data = Student.objects.create(stu_name='Ramkumar',stu_email='ramkumar@gmail.com',stu_contact=852741963,stu_password=789)
#     print(data.id, data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
#     my_data={
#         'nm':data.stu_name,
#         'em':data.stu_email,
#         'con':data.stu_contact,
#         'pas':data.stu_password
#     }
#     return render (request,'dashboard.html',my_data)

# def get_or_create(request):
#     data,created = Student.objects.get_or_create(stu_name='Neeraj Kumar',stu_email='neerajkumar@gmail.com',stu_contact=963852741,stu_password=123)
#     print(data.id, data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
#     print(created)
#     my_data={
#         'nm':data.stu_name,
#         'em':data.stu_email,
#         'con':data.stu_contact,
#         'pas':data.stu_password
#     }
#     return render (request,'dashboard.html',my_data)

# def update(request):
#     data = Student.objects.filter(id=9).update(stu_name='Ravi Thakur',stu_email='ravithakur@gmail.com',stu_contact=753951748,stu_password=159)
    
#     return HttpResponse(data)

# def delete(request):
#     # data = Student.objects.get(id=14).delete() or
#     data = Student.objects.filter(id=11)
#     if data:
#         data.delete()
#         # data = Student.objects.filter(stu_name = "Neeraj").delete()
#         # print(data)
#         return HttpResponse(data)
#     else:
#         msg="This Data does not exist"
#         return render(request, 'home.html', {'msg':msg})

# def count(request):
#     data=Student.objects.all()
#     print(data.count())

# def explain(request):
#     data = Student.objects.explain()
#     print(data)

# def update_or_create(request):
#     data,created = Student.objects.update_or_create(stu_name='Ravi',stu_email='ravi@gmail.com',stu_contact=753951748,stu_password=596)
#     print(data)
#     print(created)
#     return HttpResponse(data)
#     data = Student.objects.all()
#     print(data)

# def bulk_create(request):
#     data = Student.objects.bulk_create([Student(stu_name="Neeraj",stu_email="Neeraj@gmail.com",stu_city='Indore'),Student(stu_name="Raj" ,stu_email="Raj@gmail.com",stu_city='Jabalpur'),Student(stu_name="Arvind" ,stu_email="Arvind@gmail.com",stu_city='Mandala')
#     ])
#     print(data)
#     return HttpResponse(data)

# def fillter_update(request):
#     data = Student .objects.filter(id=11).update(stu_name="ravi",stu_email="ravi@gmail.com",stu_city='Mandala')
#     print(data)
#     return HttpResponse(data)

# def get_delete(request):
#     # data=Student.objects.get(id=11).delete()
#     data=Student.objects.get(id=11)
#     data.delete()
#     return HttpResponse(data)

# def fillter_delete(request):
#     data=Student.objects.filter(id=11).delete()
#     return HttpResponse(data)

# ====================== Multipal Objects ======================= 

# def all_details(request):
#     data=Student.objects.all().values()
#     print(data)
#     print(data)
#     return render (request,'dashboard.html',{'data':data})

# def filter(request):
#     data=Student.objects.filter(stu_name='Rahul Lokhande')
#     print(data.values)
#     return render (request,'dashboard.html',{'data':data})

# def exclude(request):
#     data=Student.objects.exclude(stu_name='Rahul Lokhande')
#     print(data)
#     return render (request, 'dashboard.html', {'data':data})
# #  Ye name vala data chodh ke baki sab data aayega

# def assending(request):
#     data=Student.objects.order_by('stu_name')
#     print(data)
#     return render (request, 'dashboard.html', {'data':data})

# def decending(request):
#     data=Student.objects.order_by('stu_name').reverse()
#     print(data)
#     return render (request, 'dashboard.html', {'data':data})

# def decending2(request):
#     data=Student.objects.order_by('-stu_name')
#     print(data)
#     return render (request, 'dashboard.html', {'data':data})

# def rendom(request):
#     data=Student.objects.order_by("?")
#     print(data)
#     return render (request, 'dashboard.html', {'data':data})

def slice(request):
    data=(Student.objects.all().order_by('-id')[:5])
    # data=(Student.objects.order_by('id').reverse()[:5])
    print(data)
    return render (request, 'dashboard.html', {'data':data})

def query(request):
    if request.method=="POST":
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        query1=request.POST.get('query')

        print(name1,email1,query1)

        Query.objects.create(name=name1, email=email1, query=query1)
        data=Student.objects.get(stu_email=email1)
        my_data={
            'nm':data.stu_name,
            'em':data.stu_email,
            'con':data.stu_contact,
            'pas':data.stu_password
        }
        print(my_data)
        all_query=Query.objects.filter(email=email1)
        return render(request, 'dashboard.html',{'key1':all_query,'data':my_data})
    else:
        return render(request, 'dashboard.html')
        
# def delete(request,pk):
#     data=Query.objects.get(id=pk)
#     email=data.email
#     data.delete()
#     all_data
#     return render(request, 'dashboard.html')

def edit(request, x):
    user_data=Query.objects.get(id=x)
    id1 = user_data.id
    email=user_data.email
    name=user_data.name
    query=user_data.query
    print(query)
    data=Student.objects.get(stu_email=email)
    my_data={
            'nm':data.stu_name,
            'em':data.stu_email,
            'con':data.stu_contact,
            'pas':data.stu_password
        }
    all_query=Query.objects.filter(email=email)
    print(all_query)
    edit_data={
        'id':id1,
        'nm':name,
        'em':email,
        'qu':query
    }
    print(edit_data)
    return render(request, 'dashboard.html', {'key1':all_query, 'data':my_data,'edit':edit_data })

def update(request,x):
    if request.method=="POST":
        oldData=Query.objects.get(id=x)
        
        name1=request.POST['name']
        email1=request.POST['email']
        query1=request.POST['query']
        print(name1,email1,query1,x)
        
        oldData.name=name1
        oldData.email=email1
        oldData.query=query1

        oldData.save()
        
        
        
    return render(request, 'dashboard.html', {'key1':all_query, 'data':my_data })



