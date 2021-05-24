from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='images/', blank=True,default='images/smiley-4832482_1920.png')
    bio=models.CharField(max_length =100,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username 
        

    @classmethod
    def get_profile(cls,user_id):
        userd=cls.objects.get(user=user_id)
        # print (userd)
        return userd;
    @classmethod
    def update(cls,user_id):
        pass
