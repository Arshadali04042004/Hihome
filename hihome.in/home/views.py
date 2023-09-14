from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Registration,Contactus,myuploadfile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def upcomming(request):
    return render(request,'upcomming.html')

    



def contactus(request):
    if request.method == "POST":
        contactName = request.POST.get('contactName')
        contactEmail = request.POST.get('contactEmail')
        contactMessage = request.POST.get('contactMessage')
        contactus = Contactus(contactName=contactName,contactEmail=contactEmail,contactMessage=contactMessage)
        contactus.save()
        messages.success(request,'Message sent successfully ! Thanks for contacting us ...')
    return render(request,'contactus.html')



def registration(request):
    if request.method == "POST" :
        
        
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phone = request.POST.get('phone')
        competetions = request.POST.get('competetions')
        zip = request.POST.get('zip')
        
        registration = Registration(name=name,phone=phone,lastname=lastname,email=email,address=address,city=city,state=state,zip=zip,competetions=competetions,date=datetime.today())
        registration.save()
        
     
        return redirect('/upload')
    
    return render(request,'registration.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        confirm_password = request.POST['confirm_password']
        if pass1==confirm_password:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.save()
            messages.success(request,"New account is created Login Now !")
            return redirect('/')
            
        else:
            messages.success(request,"Password not matched , try again !")
            
    return render(request,'signup.html')

    #else:
        # return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == "POST":
        loginUsername = request.POST['loginUsername']
        loginPassword = request.POST['loginPassword']

        user = authenticate(username=loginUsername,password=loginPassword)

        if user is not None:
            login(request,user)
           
            messages.success(request,f"Welcome {request.user}, You successfully logged in !")
            return redirect('/')
        else:
            messages.error(request,"Invalid Username or Password, Please try again !")
            return redirect('/')

        return HttpResponse('handleLogin')

def handleLogout(request):
    
    logout(request)
    messages.success(request,"Successfully Logged Out !")
    return redirect('/')
    
def comp1(request):
    return render(request,'comp1.html')
    

def send_files(request):
    if request.method == "POST":
        f_name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadFiles")
        
        for i in myfile:
            myuploadfile(myfile=i,f_name=f_name).save()
            messages.success(request,"File Uploaded !")
        
    return render(request,'send_files.html')