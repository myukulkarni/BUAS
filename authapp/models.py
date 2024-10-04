from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contact_no = models.CharField(max_length=10, null=True)
    Gender = models.CharField(max_length=10, null=True)
    date_of_birth = models.DateField(null=True)
    educational_status = models.CharField(max_length=100, null=True)
    university = models.CharField(max_length=100, blank=True, null=True)
    residential_adress = models.CharField(max_length=100, blank=True, null=True)
    
    is_verified = models.BooleanField(default=False)
