from django import forms
from django.forms import ModelForm
from .models import UserProfile

class SignUpForm(ModelForm):
    #password = forms.CharField(blank=True)
    password = forms.CharField(required = False) 
    class Meta:
        
        model = UserProfile
        fields = '__all__'

class SignInForm(forms.Form):   
    mobile=forms.CharField(max_length=11)
    password=forms.CharField(max_length=20)        