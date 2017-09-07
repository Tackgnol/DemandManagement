from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from Engagement.models import SubProject, Activity

# Create your models here.

class Section(models.Model):
    Name = models.CharField(max_length = 100)
    Title = models.CharField(max_length = 100)
    Subheading = models.CharField(max_length = 256, blank = True, null= True)

    def __str__(self):
        return self.Name

class InputType(models.Model):
    Name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.Name


class Option(models.Model):
    Value = models.CharField(max_length=256)
    def __str__(self):
        return self.Value


class OptionGroup(models.Model):
    Name = models.CharField(max_length=75)
    Options = models.ManyToManyField(Option)
    def __str__(self):
        return self.Name

class Unit(models.Model):
    Name = models.CharField(max_length = 50)
    def __str__(self):
        return self.Name
    
class Question(models.Model):
    Section = models.ForeignKey(Section)
    InputType = models.ForeignKey(InputType)
    Text = models.CharField(max_length = 256)
    AnswerRequired = models.BooleanField(default=False, blank=False, null=False)
    MultipleAnswers = models.BooleanField(default=False, blank=False, null=False)
    OptionGroup = models.ForeignKey(OptionGroup,blank=True, null=True)
    Unit = models.ForeignKey(Unit, blank=True, null=True)

    def __str__(self):
        return self.Text

class QuestionSet(models.Model):
    Name = models.CharField(max_length = 256)
    Questions = models.ManyToManyField(Question)
    DefaultFor = models.OneToOneField(Activity, null=True, blank=True)

    def __str__(self):
        return self.Name

class Survey(models.Model):
    Respondent = models.ForeignKey(User)
    Engagement = models.ForeignKey(SubProject)
    QuestionSet = models.ForeignKey(QuestionSet)

    def __str__(self):
        return self.Engagement.Name + ' - ' + self.QuestionSet.Name

class Answer(models.Model):
    Question = models.ForeignKey(Question)
    Survey = models.ForeignKey(Survey, null=True)
    Options = models.ManyToManyField(Option, blank=True)
    Numeric = models.FloatField(null=True, blank=True)
    Text = models.CharField(max_length = 1000, null = True, blank=True)
    Bool = models.NullBooleanField( null = True, blank=True)
    
    
    def __str__(self):
        question = self.Question.Text
        if not self.Text is None:
            return question + ' - ' + self.Text
        if not self.Numeric is None:
            return question + ' - ' + str(self.Numeric)
        if not self.Bool is None: 
            return question + ' - ' + str(self.Bool)

        return question + ' - ' + 'No answer specified delete or fix.'
    




