from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=50)
    Type = models.CharField(choices = [('Product','Product'),('servies','services')], max_length=8)
    Client = models.CharField(max_length=80, null=True, blank=True)
    Description = models.TextField()
    Start_Date = models.DateField(max_length=8)
    Budget = models.IntegerField(verbose_name='Budget (in $)')
    Deadline = models.DateField(max_length=8)
    status = models.TextField(choices=[('Under Development','Under Development'),('Aborted','Aborted'),('Delivered','Delivered'),('Running','Running')])
    Manager = models.OneToOneField('employees.Manager', on_delete = models.SET_NULL,  null=True)

class Project(models.Model):
    Description = models.TextField()
    Product = models.ForeignKey('Product',  on_delete = models.CASCADE)
    Employee = models.ForeignKey('employees.Employee', on_delete = models.SET_NULL, null=True)
    Status = models.TextField(choices=[('Completed','Completed'),('Pending','Pending')])
