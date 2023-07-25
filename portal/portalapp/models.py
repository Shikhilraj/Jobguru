from django.db import models
from django.contrib.auth.models import User
class registermodel(models.Model):
    name=models.CharField(max_length=20)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    birthday=models.DateField()
    password= models.CharField(max_length=20)
    qualification=models.CharField(max_length=50)

class c_registermodel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class addjobmodel(models.Model):
    company_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    jobtitle = models.CharField(max_length=20)

    WORK_TYPES = [
        ("hybrid", "Hybrid"),
        ("rural", "Rural"),
        ("city", "City")
    ]
    worktype = models.CharField(max_length=20, choices=WORK_TYPES)
    Experiences=[
        ("parttime","PartTime"),
        ("fulltime","FullTime")
    ]
    experience = models.CharField(max_length=20, choices=Experiences)
    job_type = models.CharField(max_length=20)

class applyjobmodel(models.Model):
    companyname = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    qualification=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    experience=models.CharField(max_length=50)
    resume=models.ImageField(upload_to='portalapp/static')

