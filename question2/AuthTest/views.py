from django.shortcuts import render,HttpResponse,redirect
from .models import UserProfile
import random
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def send_Password(request,mobile):
    password = random.randint(1000, 9999)
    #mobile=request.GET["mobile"]

    #send password to mobile number
    user=UserProfile.objects.filter(mobile=mobile).first()
    user.temp_password=str(password)
    user.save()
    return password

@csrf_exempt   
def check_temporary_password(request):
    if request.method == 'POST': 
        #mobile=request.POST.get("mobile")
        mobile=request.GET["mobile"]
        temp_password=request.POST.get("temp_password")
        user=UserProfile.objects.filter(mobile=mobile).first()
        if(user.temp_password == temp_password):
            return HttpResponse("user Athenticate")
        else:
            return HttpResponse("password is wrong")    

@csrf_exempt
def signUp(request):
    if request.method == 'GET':
        return HttpResponse("signup page")

    elif request.method == 'POST':    
        mobile=request.POST.get("mobile")
        if (not UserProfile.objects.filter(mobile=mobile).exists()):
            name=request.POST.get("name")
            family=request.POST.get("family")
            gender=request.POST.get("gender")
            birth_date=request.POST.get("birth_date")
            email=request.POST.get("email")
            location=request.POST.get("location")
            password=request.POST.get("password")
            user = UserProfile(name=name, family=family, mobile=mobile, gender=gender, birth_date=birth_date, email=email, location=location, password=password)
            user.save()
            return HttpResponse("user signed up")

    return HttpResponse("can't signup")   

@csrf_exempt
def signIn(request):
    if request.method == 'GET':
        return HttpResponse("login page")

    elif request.method == 'POST':          
        mobile=request.POST.get("mobile")
        if (UserProfile.objects.filter(mobile=mobile).exists()):
            password=request.POST.get("password")
            user=UserProfile.objects.filter(mobile=mobile).first()
            if(user.password == password):
                if(password == ""):
                    temp_password=send_Password(request,mobile)
                else:    
                    request.session['login']=True
                    return HttpResponse("user "+str(mobile)+" loged in")
               
    return HttpResponse("can't login")


