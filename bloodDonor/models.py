from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BloodDonnor(models.Model):
    bloodType=[
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-')
    ]
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    user=models.OneToOneField(User , on_delete=models.CASCADE)
    birth_day=models.DateField(default=timezone.now)
    blood_type=models.CharField(max_length=3, choices=bloodType)
    def __str__(self):
        return self.user.username
# Create your models here.
