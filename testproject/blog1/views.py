from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import *

# Create your views here.

def admin_reg(request):
    
    
    return render(request, 'admin_reg.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                return redirect('admin_log')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                user.save()
                return redirect('admin_log')
        else:
            return redirect('admin_reg')
    else:
        return redirect('admin_reg')
    
def admin_log(request):
    return render(request, 'admin_log.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        
        user = auth.authenticate(username=username,password=password)
        
        
        if user is not None:
            auth.login(request,user)
            
            return redirect('company_reg')
        else:
            return redirect('admin_log')
    else:
        return redirect('admin_log')
    
def company_reg(request):
    
    return render(request, 'company_reg.html')

def company_save(request):
    if request.method == 'POST':
        name = request.POST['name']
        companytype = request.POST['company_type']
        businessname = request.POST['business_name']
        email = request.POST['email']
        phonenumber = request.POST['phone_number']
        website = request.POST['website']
        city = request.POST['city']
        state = request.POST['State']
        country = request.POST['Country']
        pincode = request.POST['Pincode']
        companylogo = request.FILES['company_logo']
        x = User.objects.get(id=request.user.id)
        
        print(request.user.username)
        
        win = Company(name=name,company_type=companytype,business_name=businessname,email=email,phone_number=phonenumber,website=website,
                      city=city,State=state,Country=country,Pincode=pincode,company_logo=companylogo,userid=x)

        win.save()
        
       
        
        return redirect('branch_reg')
    else:
        return redirect('company_reg')
    
def branch_reg(request):
    pr = Company.objects.all()
    return render(request, 'branch_reg.html',{'pr':pr})
        