from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
                messages.info(request, 'Registration successfully completed')
                return redirect('admin_log')
        else:
            messages.info(request, 'password not matching')
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
            messages.info(request, 'login successfully')
            return redirect('company_reg')
        else:
            messages.info(request, 'Username or password incorrectly')
            return redirect('admin_log')
    else:
        return redirect('admin_log')
 

@login_required(login_url='admin_log')
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
        if Company.objects.filter(userid=x).exists():
            return redirect('company_reg')
        
        elif Company.objects.filter(business_name=businessname).exists():
            return redirect('company_reg')
         
        else:
            
            win = Company(name=name,company_type=companytype,business_name=businessname,email=email,phone_number=phonenumber,website=website,
                        city=city,State=state,Country=country,Pincode=pincode,company_logo=companylogo,userid=x)

            win.save()
        
       
            messages.info(request, 'Company registration successfully')
            return redirect('branch_reg')
    else:
        messages.info(request, 'Registration Failed')
        return redirect('company_reg')
    
    
@login_required(login_url='admin_log')
def branch_reg(request):
    x = User.objects.get(id=request.user.id)
    pr = Company.objects.get(userid=x)
    return render(request, 'branch_reg.html',{'pr':pr})

def logout(request):
    auth.logout(request)
    return redirect('admin_reg')
        