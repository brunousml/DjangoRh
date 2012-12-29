from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')
    email = models.EmailField()
    status = models.BooleanField()
    phone = models.CharField(max_length=200)
    birth = models.DateField()
    create_at = models.DateTimeField('date published')

class Department(models.Model):
    employee = models.ForeignKey(Employees)
    create_at = models.DateTimeField('date published')

class Position(models.Model):
    employee = models.ForeignKey(Employees)
    create_at = models.DateTimeField('date published')