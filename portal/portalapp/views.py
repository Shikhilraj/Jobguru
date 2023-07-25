from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from portal.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
import uuid



def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        a =registerform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            em=a.cleaned_data['email']
            dob=a.cleaned_data['birthday']
            phone=a.cleaned_data['phonenumber']
            pas=a.cleaned_data['password']
            cpas=a.cleaned_data['password1']
            if pas == cpas:
                b=registermodel(name=nm,email=em,birthday=dob,phonenumber=phone,password=pas)
                b.save()
                # return HttpResponse("Saved successfully")
                return redirect(login)
            else:
                return HttpResponse("password mismatch")
        else:
            return HttpResponse("Enter Valid data")
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
                em=a.cleaned_data['email']
                pas=a.cleaned_data['password']
                b=registermodel.objects.all()
                for i in b:
                    if em ==i.email and pas==i.password:
                        name=i.name
                        email=i.email
                        ph=i.phonenumber
                        dob=i.birthday
                        qli=i.qualification
                        id=i.id

                        #return HttpResponse("Success")
                        return render(request,'userprofile.html',{'name':name,'email':email,'ph':ph,'birthday':dob,'qli':qli,'id':id})
                else:
                    return HttpResponse("Email and Password incorrect")
        else:
            return HttpResponse("Login Failed")
    return render(request,"login.html")

def userprofile(request):
    a=registermodel.objects.all()
    return render(request,'userprofile.html')

def userprofile_edit(request,id):
    user=registermodel.objects.get(id=id)
    if request.method == 'POST':
        user.name=request.POST.get('name')
        user.email=request.POST.get('email')
        user.phonenumber=request.POST.get('phonenumber')
        user.dob=request.POST.get('birthday')
        user.qualification = request.POST.get('qualification')
        user.save()
        return redirect(login)
    return render(request,'userprofile_edit.html',{'user':user})
def logout(request):
    return redirect(index)


def c_register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pas = request.POST.get('password')
        cpass = request.POST.get('password1')
        if pas == cpass:
            if User.objects.filter(username=uname).first():
                messages.success(request,"username already taken")
                return HttpResponse("username already exist")
                #return redirect(c_register)
            if User.objects.filter(email=email).first():
                messages.success(request,"email already taken")
                return HttpResponse("Email already exist")
                #return redirect(c_register)
            user_obj=User(username=uname,email=email)
            user_obj.set_password(pas)
            user_obj.save()
            auth_token=str(uuid.uuid4())
            profile_obj=c_registermodel.objects.create(user=user_obj,auth_token=auth_token)
            profile_obj.save()
            send_mail_regis(email,auth_token)
            return HttpResponse("Verified successfully")
        return HttpResponse("Passowrd mismatch")
    return render(request,"company_register.html")

def send_mail_regis(email,token):
    subject="your account has been verified"
    message=f'pass the link to verify your account http:/127.0.0.1:8000/verify/{token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def c_login(request):
    global User;
    if request.method=='POST':
        a=company_loginform(request.POST)
        username = request.POST.get('c_user')
        pas = request.POST.get('password')
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'User not found')
            return redirect(c_login)
        profile_obj=c_registermodel.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile not verified check your email')
            return redirect(c_login)
        User=authenticate(username=username,password=pas)

        if User is None:
            messages.success(request,'Wrong password or None')
            return redirect(login)
        # return HttpResponse("Login successfully")
        a=c_registermodel.objects.filter(user=User)
        return render(request,'company_profile.html',{'a':a})
    return render(request,'company_login.html')

def verify(request,auth_token):
    profile_obj=c_registermodel.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account already verified')
            return redirect(c_login)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account verified')
        return redirect(c_login)
    else:
        return HttpResponse("Error")

def c_profile(request):
    a=c_registermodel.objects.all()

    return render(request,'company_profile.html')

def registercompany_list(request):
    a=c_registermodel.objects.all()
    comp=[]
    email=[]
    id1=[]
    for i in a:
        c=i.user.username
        comp.append(c)
        e=i.user.email
        email.append(e)
        k=i.user.id
        id1.append(k)
    mylist=zip(comp,email,id1)
    return render(request,'registeredcompanies.html', {"mylist": mylist})


def sendmail(request):
    if request.method=='POST' :
        a=sendmailform(request.POST)
        if a.is_valid():
            cname=a.cleaned_data['companyname']
            email=a.cleaned_data['email']
            sub=a.cleaned_data['subject']
            msg=a.cleaned_data['message']
            send_mail((str(sub)) + '||' +cname, msg, EMAIL_HOST_USER, [email], fail_silently=False)

            return HttpResponse("Mail send succefully")
        return HttpResponse('Enter Valid data')
    return render(request,"sendmail.html")

def addjob(request):
    if request.method == "POST":
        a=addjobform(request.POST)
        if a.is_valid():
            cname = a.cleaned_data['companyname']
            email = a.cleaned_data["email"]
            jobtitle=a.cleaned_data['jobtitle']
            jobtype = a.cleaned_data['jobtype']
            worktype = a.cleaned_data['worktype']
            exp = a.cleaned_data['experience']
            b = addjobmodel(company_name=cname,email=email,job_type=jobtype,worktype=worktype,experience=exp,jobtitle=jobtitle)
            b.save()
            return HttpResponse("Success")
        return HttpResponse("Enter Valid data")
    return render(request,'addjob.html')


def joblist(request,id):
    userid=id
    a=addjobmodel.objects.all()
    comp = []
    ema = []
    id1 = []
    jtitle=[]
    jobtype=[]
    wtype=[]
    exp=[]
    for i in a:
        cn = i.company_name
        comp.append(cn)
        em = i.email
        ema.append(em)
        j=i.jobtitle
        jtitle.append(j)
        jtype=i.job_type
        jobtype.append(jtype)
        id2 =i.id
        id1.append(id2)
        wk=i.worktype
        wtype.append(wk)
        ex=i.experience
        exp.append(ex)
    jobs = zip(comp,ema,id1,jtitle,jobtype,wtype,exp)
    return render(request,'joblist.html',{'jobs':jobs,'userid':userid})

def applyjob(request,id2,id1):
    #job=c_registermodel.objects.filter(id=id2)
    user = registermodel.objects.get(id=id1)
    uname=user.name
    uemail=user.email
    #cname=job.user.username
   # cjob=job.jobtitle
    mylist={'a':uname,'b':uemail} #contexct
    if request.method=='POST':
        apply=applyjobmodel()
        apply.companyname=request.POST.get('companyname')
        apply.designation=request.POST.get('designation')
        apply.username=request.POST.get('username')
        apply.email = request.POST.get('email')
        apply.qualification = request.POST.get('qualification')
        apply.phonenumber = request.POST.get('phonenumber')
        apply.experience = request.POST.get('experience')
        apply.save()
        return HttpResponse("Success")
    return render(request,'applyjob.html',mylist)

def viewapplicant(request,id):
    a=applyjobmodel.objects.all()
    # jobs=c_registermodel.objects.get(id=id)
    # comp=jobs.user.username
    comp=id
    nm=[]
    em=[]
    ph=[]
    qn=[]
    exp=[]
    ur=[]
    for i in a:
        if i.companyname == comp:
            nm1=i.username
            nm.append(nm1)
            em1=i.email
            em.append(em1)
            ph1=i.phonenumber
            ph.append(ph1)
            exp1=i.experience
            exp.append(exp1)
            ur1=i.resume
            qn1=i.qualification
            qn.append(qn1)
            ur.append(str(ur1).split('/')[-1])
    mylist=zip(nm,em,qn,ph,exp,ur)
    return render(request,'viewapplicants.html',{'mylist':mylist})
    #return HttpResponse("No Applicants Available")


def appliedjobs(request,id):
    a=applyjobmodel.objects.all()
    jobs=registermodel.objects.get(id=id)
    comp=[]
    des=[]
    em=[]
    ql=[]
    exp=[]
    res=[]
    for i in a:
        if i.id== id:
            comp1=i.companyname
            comp.append(comp1)
            des1=i.designation
            des.append(des1)
            em1=i.email
            em.append(em1)
            ql1=i.qualification
            ql.append(ql1)
            exp1=i.experience
            exp.append(exp1)
            res1=i.resume
            res.append(str(res1).split(',')[-1])
        joblist=zip(comp,em,des,ql,exp,res)
        return render(request,'appliedjobs.html',{'joblist':joblist})
            
            
            


