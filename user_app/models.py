from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RegisterForm(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=100)
    Password2 = models.CharField(max_length=100)
    
    class Meta:
       verbose_name_plural = "RegisterForms" 
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profileImage',default='profileImage/noprofile.png')
    phone = models.CharField(max_length=14,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.user.username
