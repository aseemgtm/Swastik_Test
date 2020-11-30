from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

GENDER_MALE = 'M'
GENDER_FEMALE = 'F'
GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'),]
R_M = 'Marketing'
R_B = 'Backend-Development'
R_T = 'Testing'
R_F = 'Frontend-Development'
ROLE_CHOICES =[(R_M,'Marketing'),(R_B,'Backend-Development'),(R_T,'Testing'),(R_F,'Frontend-Development')]

class Emp(models.Model):
    User = models.OneToOneField(User, on_delete = models.CASCADE)
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    DOB = models.DateField(max_length=8)
    Gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    Date_joined = models.DateField(max_length=8)
    Email = models.EmailField(max_length=60)
    Address = models.CharField(max_length=100, help_text='eg : #112 Sector 40C', default=' ')
    Contact_number = models.BigIntegerField()
    City = models.CharField(max_length = 50, default=' ')
    status = models.CharField(max_length = 6, choices=[('active','active'),('left','left')])

    def __str__(self):
        return f'{ self.first_name }' + ' ' + f'{ self.last_name }'

    class Meta:
        abstract = True

class Manager(Emp):
    pass

class Employee(Emp):
    manager = models.ForeignKey('Manager', on_delete = models.SET_NULL,  null=True)
    team = models.CharField(choices = ROLE_CHOICES, max_length = 20)