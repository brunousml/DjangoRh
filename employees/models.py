from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='uploads/')
    email = models.EmailField()
    status = models.BooleanField()
    phone = models.CharField(max_length=200)
    birth = models.DateField()
    create_at = models.DateTimeField('date published')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "%s" % (self.email)

class Department(models.Model):
    employees = models.ManyToManyField(Employees)
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField('date published')

    def __unicode__(self):
        return "%s" % (self.name)

class Position(models.Model):
    department = models.ManyToManyField(Department)
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField('date published')

    def __unicode__(self):
        return "%s" % (self.name)
    
