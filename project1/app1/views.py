from operator import contains

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def home(request):
    template_name = 'app1/home.html'
    context = {}
    return render(request, template_name, context)

def about(request):
    template_name = 'app1/about.html'
    context = {}
    return render(request, template_name, context)

def contact(request):
    print(request.POST)
    if(request.method == 'POST'):
        mail = request.POST.get('Email')
        obj = User.objects.all()
        for i in obj:
            if(i.email == mail):
                return HttpResponse('<h1>Message Send Successfully....</h1>')
        else:
            return HttpResponse('<h1>Entry Not Available</h1>')
    template_name = 'app1/contact.html'
    context = {}
    return render(request, template_name, context)

def help(request):
    print(request.POST)
    if(request.method == 'POST'):
        mail = request.POST.get('Email')
        obj = User.objects.all()
        for i in obj:
            if(i.email == mail):
                return HttpResponse('<h1>Help Working Properly</h1>')
        else:
            return HttpResponse('<h1>Entry Not Present</h1>')
    template_name = 'app1/help.html'
    context = {}
    return render(request, template_name, context)

def log_in(request):
    if(request.method == 'POST'):
        mail = request.POST.get('Email')
        obj = User.objects.all()
        for i in obj:
            if(i.email == mail):
                return redirect('home')
        else:
            return HttpResponse('<h1>Object Not Present</h1>')
    template_name = 'app1/Log_in.html'
    context = {}
    return render(request, template_name, context)

def sign_up(request):
    if(request.method == 'POST'):
        first = request.POST.get('First_Name')
        last = request.POST.get('Last_Name')
        mobile = request.POST.get('Mobile')
        gender = request.POST.get('gender')
        email = request.POST.get('Email')
        password = request.POST.get('password')

        record = User.objects.all()
        for i in record:
            if(i.email == email):
                return redirect('login')

        obj = User(first=first,last=last,mobile=mobile,gender=gender,email=email,password=password)
        obj.save()
        return redirect('home')

    template_name = 'app1/sign_up.html'
    context = {}
    return render(request, template_name, context)

# Here are all the views content