from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')