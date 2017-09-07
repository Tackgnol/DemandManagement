from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView, CreateView, ListView, DetailView
from models import Question, Answer, Option, OptionGroup, QuestionSet, Survey
from templatetags import SurveyExtras
# Create your views here.


def GetFormOptions(request):
    return [o for o in request.POST.getlist('Options')]

def DefaultList(request):
    defaultList = []
    for q in QuestionSet.objects.all():
        if not q.DefaultFor is None:
            defaultList.append(str(q.DefaultFor.pk))
    return defaultList

def GetOption(value):
    return Option.objects.get(Value=value)

def GetQuestion(pk):
    return Question.objects.get(pk=pk)

def GetInstanceOptionGroup(form):
    question = get_object_or_404(Question, pk=form.instance.pk)
    return question.OptionGroup

class NewSurvey(CreateView):
    model = QuestionSet
    fields = ('Name', 'DefaultFor')
    template_name = 'Survey/CreateSurvey.html'
    context_object_name = 'Survey'
    success_url = "/Survey/NewSurvey/"

    def Questions(self):
        return Question.objects.all()

    def form_valid(self, form):
        questionSet = form.instance
        questionSet.save()
        for option in self.request.POST.getlist('selectedQuestions'):
            questionSet.Questions.add(GetQuestion(option))
        form.save()
        return super(NewSurvey, self).form_valid(form)

    def form_invalid(self, form):
        response = super(NewSurvey, self).form_invalid(form)
        req = self.request
        defaultsUsed = DefaultList(self.request)
        if req.POST.get('DefaultFor') in defaultsUsed:
            messages.error(req, 'This Activity already has a default survey, leave the ')
        if req.POST.get('Name') is None:
            messages.error(req, 'No Name specified')
        return response

class FillSurvey(UpdateView):
    model = Survey
    fields = ()
    template_name = 'Survey/Survey.html'
    context_object_name = 'Survey'
    success_url = "/Survey/"

    def Answers(self):
        return Answer.objects.filter(Survey=self.kwargs['pk'])

    def form_valid(self, form):
        Questions = form.instance.QuestionSet.Questions.all()
        request = self.request.POST
        form.clean()
        for question in Questions:
            if request.__contains__(str(question.pk)) and request.get(str(question.pk)) != '':
                if Answer.objects.filter(Question = question.pk, Survey = form.instance.pk).exists():
                    newAnswear = Answer.objects.get(Question=question.pk, Survey=form.instance.pk)
                    newAnswear.Options.clear()
                else:
                    newAnswear = Answer(Question=question, Survey=form.instance)
                    newAnswear.save()
                if question.InputType.pk == settings.TEXT_ID:
                    newAnswear.Text =  request.get(str(question.pk))
                if question.InputType.pk == settings.NUMERIC_ID:
                    newAnswear.Numeric = request.get(str(question.pk))
                if question.InputType.pk == settings.BOOL_ID:
                    newAnswear.Bool = bool(int(request.get(str(question.pk))))
                if question.InputType.pk == settings.OPTIONS_ID:
                    for option in request.getlist(str(question.pk)):
                        selectedOption = GetOption(option)
                        newAnswear.Options.add(selectedOption)
                newAnswear.save()
            else:
                if Answer.objects.filter(Question = question.pk, Survey = form.instance.pk).exists():
                    Answer.objects.filter(Question = question.pk, Survey = form.instance.pk).delete()
            
        return super(FillSurvey, self).form_valid(form)



class AllSurveys(ListView):
    model = Survey
    template_name = "Survey/AllSurveys.html"
    context_object_name = "Surveys"

    
class NewQuestion(CreateView):
    model = Question
    fields = '__all__'
    template_name = 'Survey/CreateUpdateQuestion.html'
    context_object_name = 'Question'
    success_url="/Survey/"

    def form_valid(self, form):
        if form.instance.InputType.pk == settings.OPTIONS_ID:
            
            newOptionGroup = OptionGroup(Name = form.instance.Text + ' Answer Group')
            newOptionGroup.save()
            for option in GetFormOptions(self.request):
                newOption = Option(Value = option)
                newOption.save()
                newOptionGroup.Options.add(newOption)            
            newOptionGroup.save()
            form.instance.OptionGroup = newOptionGroup
            form.save()
            return super(NewQuestion, self).form_valid(form)


        return super(NewQuestion, self).form_valid(form)

    def form_invalid(self, form):
        print('Form was invalid')
        return super(NewQuestion, self).form_invalid(form)


class UpdateQuestion(UpdateView):
    model = Question
    template_name = 'Survey/CreateUpdateQuestion.html'
    context_object_name = 'Question'
    success_url="/Survey/"
    fields = '__all__'

    def form_valid(self, form):
        if form.instance.InputType.pk == settings.OPTIONS_ID:
            formOptions = GetFormOptions(self.request)
            instanceOptionGroup = GetInstanceOptionGroup(form)
            if instanceOptionGroup != None:
                for option in instanceOptionGroup.Options.all():
                    if option.Value in formOptions:
                        formOptions.remove(option.Value)
                    else:
                        instanceOptionGroup.Options.remove(option)
                        option.delete(keep_parents=True)
            else:
                instanceOptionGroup = OptionGroup(Name=form.instance.Text + "Answer Group")
                instanceOptionGroup.save()
                form.instance.OptionGroup = instanceOptionGroup

            for newOption in formOptions:
                newOptionObject = Option(Value = newOption)
                newOptionObject.save()
                instanceOptionGroup.Options.add(newOptionObject)
            
            instanceOptionGroup.save()
            form.instance.OptionGroup = instanceOptionGroup
            form.save()
            return super(UpdateQuestion, self).form_valid(form)
        else:
            return super(UpdateQuestion, self).form_valid(form)




class ViewQuestion(DetailView):
    model = Question
    template_name = "Survey/ViewQuestion.html"
    context_object_name = 'Question'

class AllQuestions(ListView):
    model = Question
    template_name = "Survey/AllQuestions.html"
    context_object_name = 'Questions'
