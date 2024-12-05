from django.shortcuts import render,redirect
from .models import User
from django.core.mail import send_mail



# Create your views here.
def IndexView(request):
    return render(request,"Task_Management_App/index.html") #Index.html View
#register html page view
def RegisterView(request):
    return render(request,"Task_Management_App/register.html") #Register.html View
#insert user view
def insertuser(request):
    if request.method=="POST":
        vnm=request.POST['tname']
        vem=request.POST['temail']
        vph=request.POST['tphone']
        vdeg=request.POST['tdesignation']
        vdep=request.POST['tdepartment']
        vid=request.POST['tid']
        vpas=request.POST['tpass']
        us=User(nm=vnm,em=vem,ph=vph,dg=vdeg,dp=vdep,ofid=vid,pas=vpas)
        us.save()
        return render(request, 'Task_Management_App/register.html', {'msg': 'User created successfully!'})
    else:
        return render(request,'Task_Management_App/register.html',{})

#login html view
def LoginView(request):
    return render(request,"Task_Management_App/login.html")

def ShowView(request):
    return render(request,"Task_Management_App/show.html")

#login function view
def loginuser(request):
    if request.method=="POST":
        email=request.POST['temail']
        password=request.POST['tpass']
        user=User.objects.get(em=email)

        if user:
            if user.pas != password:
                request.session['Name']=user.nm
                request.session['Desgination']=user.dg
                request.session['Department']=user.dp
                request.session['OfficeId']=user.ofid
                return render(request,"Task_Management_App/show.html")
               # return render(request,"Task_Management_App/login.html",{'msg':message})
        else:
            message="User does not exsist"
            return render(request,"Task_Management_App/login.html",{'msg':message})


# Email.html page view
def EmailView(request):
           send_mail(
                "Technical Issue Resolve",
                "Here is the demo message from the user for Technical trouble.",
                "daithankarchinmayee1409@gmail.com",
                ["taskmanagementsystem40@gmail.com"],
                fail_silently=False,
                )
           message="Email Send Sucessfuly"
           return render(request,"Task_Management_App/email.html",{'msg':message})

def Perform_View(request):
    return render(request,"Task_Management_App/perform.html")

#########################################################################################
#views.py

