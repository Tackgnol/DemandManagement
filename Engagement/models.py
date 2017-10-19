from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.core import serializers
from Demand.models import Category, BusinessPriority, Activity, Project
from collections import OrderedDict
from itertools import chain
import datetime
import re
import operator


class SetArea(models.Model):
    Name = models.CharField(max_length=256)
    class Meta:
        verbose_name_plural = 'SetAreas'
    def __str__(self):
        return self.Name


class RequestType(models.Model):
    Name = models.CharField(max_length=256)
    Activity = models.ForeignKey(Activity)
    class Meta:
        verbose_name_plural = 'RequestTypes'
    def __str__(self):
        return self.Name + ' - ' + self.Activity.Name

class Complexity(models.Model):
    Name =models.CharField(max_length=10)
    class Meta:
        verbose_name_plural = 'Complexities'
    def __str__(self):
        return self.Name

class SubStatus(models.Model):
    Name = models.CharField(max_length=100)
    class Meta: 
        verbose_name_plural = 'SubStatuses'
    def __str__(self):
        return self.Name

class Step(models.Model):
    Order = models.PositiveIntegerField()
    Name = models.CharField(max_length=256)
    Activity = models.ForeignKey(Activity)
    class Meta:
        verbose_name_plural = 'Steps'
    def __str__(self):
        return self.Activity.Name + ' - ' + self.Name
    

class SubProject(models.Model):
    Project = models.ForeignKey(Project,null=True)
    Activity = models.ForeignKey(Activity, null=True)
    Active = models.BooleanField()
    CreatedDate = models.DateTimeField(auto_now_add=True)
    LastUpdated = models.DateTimeField(auto_now=True)
    Requestor = models.ForeignKey(User, related_name='Requestor')
    ForSetArea = models.ForeignKey(SetArea, null=True )
    Name = models.CharField(max_length=256, null=True)
    Step = models.ForeignKey(Step)
    Categories = models.ManyToManyField(Category, blank=True)
    Specialist = models.ForeignKey(User, related_name='Specialist', null=True)
    Type = models.ForeignKey(RequestType,null=True)
    Complexity = models.ForeignKey(Complexity,blank=False, null=True)
    Details = models.CharField(max_length=1000, blank=True)
    Priority = models.ForeignKey(BusinessPriority,null=True)
    Deadline = models.DateField(null=True, blank=True)
    AdjustedDeadline = models.DateField(blank=True, null=True)
    Status = models.ForeignKey(SubStatus)
    Completed = models.DateField(blank=True, null=True)
    Comments = models.CharField(max_length=1000, blank=True)
    class Meta:
        verbose_name_plural = 'SubProjects'
    def __str__(self):
        if self.Name == None:
            return '-'
        else:
            return self.Name
    def GenerateUserSuggestions(self):
        startDate = self.Project.StartDate
        endDate = self.Project.EndDate

        collidingProjects = Project.objects.exclude(EndDate__lte = startDate).exclude(StartDate__gte = endDate)
        collidingEngagements = []
        for project in collidingProjects:
            collidingEngagements = chain(collidingEngagements, project.subproject_set.filter(Active=True))
        
        busyUsers = {}
        complexityDict = {
            "High" : 3,
            "Medium" : 2, 
            "Low": 1,
            "None": 0
        }
        for project in collidingEngagements:
            if not project.Specialist in busyUsers:
                busyUsers[project.Specialist] = complexityDict[str(project.Complexity)]
            else:
                busyUsers[project.Specialist] += complexityDict[str(project.Complexity)]
        busyUsers = OrderedDict(sorted(busyUsers.items(), key=lambda t: t[1], reverse=True))
        return busyUsers

    def GenerateGanntValues(self):
        phases =  self.projectmanagement_set.all()
        output = '['
        previous = 'null'
        for phase in phases:
            if phase == phases[len(phases)-1]:
                end = ']'
            else: 
                end = '], '
            output = output + "['" + str(phase.Step.Order) + "', " 
            output = output + "'" + phase.Step.Name + "'"  + ', '
            output = output + 'new Date(' +str(phase.StartDate.year) + ', ' + str(phase.StartDate.month-1) + ', ' + str(phase.StartDate.day) + '), '
            output = output + 'new Date(' + str(phase.EndDate.year) + ', ' + str(phase.EndDate.month-1) + ', ' + str(phase.EndDate.day) + '), '
            output = output + 'daysToMilliseconds(' + str((phase.EndDate - phase.StartDate).days) + '), '
            output = output + str(phase.Completed * 100) + ', '
            output = output + previous if previous == 'null' else output + "'" + previous + "'"
            output = output + end
            previous =  str(phase.Step.Order)
        output = output + ']'
        output = output.decode()
        output = output.encode(encoding='utf8')
        return output
    def GenerateGanttJSON(self):
        phases = self.projectmanagement_set.all()
        data = serializers.serialize('json', phases)
        return data
        
# Create your models here.
class ProjectManagement(models.Model):
    Completed = models.BooleanField(default=False)
    Step = models.ForeignKey(Step)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    LastUpdated = models.DateTimeField(auto_now=True)
    SubProject = models.ForeignKey(SubProject)
    StartDate = models.DateField(blank=True, null=True)
    EndDate = models.DateField(blank=True, null=True)
    Comments = models.CharField(max_length=1000, blank=True)
    class Meta:
        verbose_name_plural = 'ProjectManagementActivities'    
    def __str__(self):
        return self.Step.Name 
    

class Note(models.Model):
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Engagement = models.ForeignKey(SubProject)
    Text = models.TextField(max_length=10000)

class EventLog(models.Model):
    CreatedDate = models.DateTimeField(auto_now_add=True)
    By = models.ForeignKey(User)
    Action = models.TextField(max_length=256)
    Engagement = models.ForeignKey(SubProject)