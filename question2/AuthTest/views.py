from django.shortcuts import render,HttpResponse,redirect
from .models import UserProfile
from .forms import SignInForm,SignUpForm
import random

# Create your views here.
def signUp(request):
    if request.method == 'GET':
        form=SignUpForm()

    elif request.method == 'POST':
        
        mobile=request.POST.get("mobile")
        form = SignUpForm(request.POST)
        if form.is_valid():
            if (not UserProfile.objects.filter(mobile=mobile).exists()):
                name=request.POST.get("name")
                family=request.POST.get("family")
                gender=request.POST.get("gender")
                birth_date=request.POST.get("birth_date")
                email=request.POST.get("email")
                location=request.POST.get("location")
                password=request.POST.get("password")
                user = UserProfile(name=name, family=family, mobile=mobile, gender=gender, birth_date=birth_date, email=email,
                 location=location, password=password)
                user.save()
                return redirect(signIn)

    return render(request,'signup.html', {"form": form})   


def signIn(request):
    if request.method == 'GET':
        form=SignInForm()

    elif request.method == 'POST':       
        mobile=request.POST.get("mobile")
        form = SignInForm(request.POST)
        if form.is_valid():
            if (UserProfile.objects.filter(mobile=mobile).exists()):
                password=request.POST.get("password")
                user=UserProfile.objects.filter(mobile=mobile).first()
                if(user.password == password):
                    request.session['login']=True
                    return HttpResponse("user login")
               
    return render(request,'signin.html', {"form": form})


def send_Password(request):
    password = random.randint(1000, 9999)
    mobile=request.GET["mobile"]

    #send password to mobile number
    user=UserProfile.objects.filter(mobile=mobile).first()
    user.password=str(password)
    user.save()
    return redirect(signIn)
