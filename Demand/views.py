from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.admin.widgets import AdminDateWidget
from Demand.models import Project, Category
from Engagement.models import SubProject, Step, SubStatus, Activity, ProjectManagement
import datetime
from math import floor
# Create your views here.


def GetStep(stepID):
    return Step.objects.get(pk=stepID)

def GetSubStatus(substatusId):
    return SubStatus.objects.get(pk=substatusId)

def GetProject(projectId):
    return Project.objects.get(pk=projectId)

def GetActivity(activityId):
    return Activity.objects.get(pk=activityId)

def GetCategory(categoryId):
    return Category.objects.get(pk=categoryId)

def SplitWorkdays(startDate, endDate, count):
    daygenerator = (startDate + datetime.timedelta(x+1) for x in xrange((endDate - startDate).days))
    dayList = [ day for day in daygenerator if day.weekday() < 5]
    dayCount = len(dayList)

    dayDelta = floor(dayCount/count)
    Periods = []
    timePeriod = []
    i=0
    for day in dayList:
        if timePeriod == []:
            timePeriod.append(day)
            i=0
        if i==dayDelta-1:
            timePeriod.append(day)
            Periods.append(timePeriod)
            timePeriod = []
        else:
            i+=1
    return Periods


class DemandListView(ListView):
    model = Project
    template_name = 'Demand/index.html'
    context_object_name = 'Projects'


class MainPage(TemplateView):
    template_name = 'index.html'

class DemandCreateView(CreateView):
    model = Project
    template_name = 'Demand/create.html'
    fields = [
        'Name',
        'Owner',
        'Status',
        'Risk',
        'Categories',
        'Countries',
        'BusinessPriority',
        'Spend',
        'Savings',
        'StartDate',
        'EndDate',
        'Activities',
        'Comments',
        'Actions',
    ]
    
    success_url="/DemandManagement/"

    def form_valid(self, form):
        formEndDate = form.instance.EndDate
        form.save()
        #Saving the form for it to have a PK so I can assign it to its children
        formParent = form.instance.pk
        for activity in self.request.POST.getlist('Activities'):
            SB = SubProject(Name='[' + form.instance.Name + ']' + GetActivity(activity).Name, Active=False, Activity=GetActivity(activity), Project = GetProject(formParent), Requestor=form.instance.Owner, Step=GetStep(1), Deadline=formEndDate, Status=GetSubStatus(1))
            SB.save()
            for category in self.request.POST.getlist('Categories'):
                SB.Categories.add(GetCategory(category))
            StepsForThisActivity = Step.objects.filter(Activity = GetActivity(activity))
            PeriodList = SplitWorkdays(form.instance.StartDate, form.instance.EndDate, len(StepsForThisActivity))
            i=0
            for step in StepsForThisActivity:
                PM = ProjectManagement(Completed = False,Step= step, SubProject=SB, StartDate=PeriodList[i][0], EndDate=PeriodList[i][1], )
                PM.save()
                i+=1
            SB.save()

        return super(DemandCreateView, self).form_valid(form)


