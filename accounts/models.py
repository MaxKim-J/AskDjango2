from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model): #하나의 유저 하나의 프로필 이상은 못만듬
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)