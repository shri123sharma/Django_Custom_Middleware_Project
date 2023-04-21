from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    com_name=models.CharField(max_length=255,null=True,blank=True)
    com_location=models.CharField(max_length=100,null=True,blank=True)

class Employee(models.Model):
    emp_name=models.CharField(max_length=255,null=True,blank=True)
    emp_id=models.IntegerField(null=True)

class City(models.Model):
    com_city=models.ForeignKey(Company,null=True,blank=True,related_name='company_city',on_delete=models.CASCADE)
    city_name=models.CharField(max_length=255,null=True,blank=True)
    city_pincode=models.CharField(max_length=6,null=True,default="232323")

class Account(models.Model):
    acc_name=models.CharField(max_length=266,null=True,blank=True)
    acc_amount=models.DecimalField(max_digits = 5,
                         decimal_places = 2)
    
    
