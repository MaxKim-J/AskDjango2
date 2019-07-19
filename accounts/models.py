from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model): #하나의 유저 하나의 프로필 이상은 못만듬
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)