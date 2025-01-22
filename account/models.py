from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , null=True)#once the user is deleted it will delete it whole profile
    email_add = models.CharField(max_length=100, unique=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_img = models.ImageField(upload_to='profile_images', default='user.png', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    gender = models.CharField(max_length=6, choices=GENDER, blank=True, null=True)
# after creating models make sure to register in admin.py in same app file

# these are the schema declaration credientials which we have to specify in model to use in database

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='account_profile'
    )
    additional_field = models.CharField(max_length=255, blank=True, null=True)