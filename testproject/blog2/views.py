from django.shortcuts import render, redirect

# Create your views here.

def br_reg(request):
    return render(request, 'br_reg.html')