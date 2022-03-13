from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    Pincode = models.IntegerField(max_length=50)
    company_logo = models.ImageField(default="default.png", upload_to="images")
    userid = models.ForeignKey(User,on_delete=models.CASCADE)











