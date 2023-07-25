from django import forms
from .models import *
from .views import *

class registerform(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    phonenumber=forms.IntegerField()
    birthday=forms.DateField()
    qualification=forms.CharField(max_length=50)
    password=forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=20)

class loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

class company_registerform(forms.Form):
    username=forms.CharField(max_length=20)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=20)

class company_loginform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)

class sendmailform(forms.Form):
    companyname=forms.CharField(max_length=20)
    email = forms.EmailField()
    subject=forms.CharField(max_length=50)
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'row': 3, 'col': 30}))

class addjobform(forms.Form):
    companyname=forms.CharField(max_length=50)
    email=forms.EmailField()
    jobtitle=forms.CharField(max_length=50)
    worktype=forms.CharField(max_length=50)
    experience=forms.CharField(max_length=50)
    jobtype=forms.CharField(max_length=50)

# class applyjobform(forms.Form):
#     username=forms.CharField(max_length=50)
#     email=forms.EmailField()
#     phonenumber=forms.IntegerField()
#     qualification=forms.CharField(max_length=50)
#     experience=forms.IntegerField()
#     resume=forms.ImageField()

