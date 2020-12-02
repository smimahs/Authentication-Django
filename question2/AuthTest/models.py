from django.db import models

# Create your models here.
Gender_CHOICES = [
    ('Mr', 'مرد'),
    ('Mrs', 'زن'),    
]

class UserProfile(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    name=models.CharField(max_length=150)
    family=models.CharField(max_length=150)
    mobile=models.CharField(max_length=11)
    gender=models.CharField(max_length=10,choices=Gender_CHOICES)
    birth_date = models.DateField(auto_now_add=True)
    email=models.CharField(max_length=150,unique=True)
    location = models.TextField()
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.mobile
        