from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Status(models.Model):
    Name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Statuses"
    def __str__(self):
        return self.Name

class Risk(models.Model):
    Name = models.CharField(max_length=50)
    def __str__(self):
        return self.Name
    

class BusinessPriority(models.Model):
    Name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "BusinessPriorities"
    
    def __str__(self):
        return self.Name

class Category(models.Model):
    Code = models.IntegerField()
    Name = models.CharField(max_length=255)
    #Projects = models.ManyToManyField(Project, blank=True)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.Code) + ' - ' + self.Name
class Region(models.Model):
    Name = models.CharField(max_length = 100)
    def __str__(self):
        return self.Name

class Country(models.Model):
    Name = models.CharField(max_length = 100)
    Region = models.ForeignKey(Region)
    class Meta:
        verbose_name_plural = "Countries"
    def __str__(self):
        return self.Name
class Activity(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=1000)
    Manager = models.ForeignKey(User)
    class Meta:
        verbose_name_plural = "Activities"
    def __str__(self):
        return self.Name

class Project(models.Model):
    Name = models.CharField(max_length = 256)
    Owner = models.ForeignKey(User)
    Status = models.ForeignKey(Status)    
    Risk = models.ForeignKey(Risk)
    Categories = models.ManyToManyField(Category, blank=True)
    Countries = models.ManyToManyField(Country, blank=True)
    BusinessPriority = models.ForeignKey(BusinessPriority, verbose_name= 'Business Priority')
    Spend = models.FloatField(blank=True, default=0)
    Savings = models.FloatField(blank=True, default=0)
    StartDate = models.DateField( verbose_name= 'Project Start Date')
    EndDate = models.DateField( verbose_name= 'Project End Date')
    LastUpadate = models.DateTimeField(auto_now=True, blank=True)
    Activities = models.ManyToManyField(Activity, blank=True, related_name='activities')
    Comments = models.CharField(max_length=1000, blank=True)
    Actions = models.CharField(max_length=255, blank=True)
    BusinessContacts = models.ManyToManyField(User, blank = True, related_name='BusinessContacts')
    BusinessPartners = models.ManyToManyField(User, blank = True, related_name='BusinessPartners')

    def __str__(self):
        return self.Name
    def GetSubProjects(self):
        return self.subproject_set.filter(Active=True)


class UserAssosiation(User):

    user = models.OneToOneField(User)


    def __str__(self):
        return self.user.username
