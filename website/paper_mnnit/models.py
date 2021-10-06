from django.db import models
from os import name
from typing import Tuple
from django.contrib.auth.models import User

class UserProfile(models.Model):
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=12, blank=True)
    gender = models.CharField(choices=GENDERS, max_length=1, default='')
    
    def __str__(self):
        return "{} - {}".format(self.id, self.auth_user.username)
