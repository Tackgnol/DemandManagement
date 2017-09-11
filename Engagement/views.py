from django.views.generic import ListView, DetailView, TemplateView, UpdateView
from django.shortcuts import get_object_or_404, redirect, reverse
from Engagement.models import SubProject, SubStatus, Activity, Note, EventLog
from django.contrib.auth.models import User
from .forms import DeleteNoteForm 

# Create your views here.

def GetSubStatus(name):
    return get_object_or_404(SubStatus, Name=name)

class SubProjectListView(ListView):
    model=SubProject
    template_name = 'Engagement/index.html'
    context_object_name = 'SubProjects'
    def get_queryset(self):
        MyProjects =SubProject.objects.filter(Active=True)
        return MyProjects


class SubProjectMyListView(ListView):
    template_name= 'Engagement/index.html'
    context_object_name = 'SubProjects'

    def get_queryset(self):
        currentUser = self.request.user
        if currentUser.is_authenticated():
            MyProjects =SubProject.objects.filter(Specialist=currentUser)
            return MyProjects
        return None


class SubProjectMyInactive(ListView):
    template_name= 'Engagement/index.html'
    context_object_name = 'SubProjects'
    
    def get_queryset(self):
        UserManagedActivities = Activity.objects.filter(Manager=self.request.user)
        MyProjects = SubProject.objects.filter(Active= False, Activity__in = UserManagedActivities)
        return MyProjects

class SubprojectActivate(UpdateView):
    model = SubProject
    template_name = 'Engagement/edit.html'
    fields = (
        'Active',
        'ForSetArea',
        'Name',
        'Complexity',
        'Step',
        'Categories',
        'Specialist',
        'Type',
        'Details',
        'AdjustedDeadline',
        'Status',
        'Comments'
    )
    success_url="/Engagement/Inactive/"
    context_object_name = 'SubProject'
    
class SubProjectDetailView(DetailView):
    model = SubProject
    template_name= 'Engagement/details.html'
    context_object_name = 'SubProject'

def AddNote(request, pk):
    thisProject = get_object_or_404(SubProject, pk=pk)
    newNote = Note(Engagement=thisProject, Text=request.POST['Note'])
    newNote.save()
    return redirect(request.META['HTTP_REFERER'])

def DeleteNote(request, pk):
    
    thisNote = get_object_or_404(Note, pk=pk)
    form = DeleteNoteForm(request.POST, instance=thisNote)
    if request.method == 'POST':
        if form.is_valid():
            thisNote.delete()
            return redirect(request.META['HTTP_REFERER'])
    return redirect('/Engagement/')

def NextStatus(request, pk):
    thisProject = get_object_or_404(SubProject, pk=pk)
    projectStatus = thisProject.Status.pk
    if projectStatus >= 1 and projectStatus < 3:
        thisProject.Status = get_object_or_404(SubStatus, pk=projectStatus+1)
        thisProject.save()
        newLog = EventLog(Engagement=thisProject, By=request.user, Action="Uplifeted the status to: " + str(thisProject.Status))
        newLog.save()
    return redirect(request.META['HTTP_REFERER'])


def PreviousStatus(request, pk):
    thisProject = get_object_or_404(SubProject, pk=pk)
    projectStatus = thisProject.Status.pk
    if projectStatus > 1 and projectStatus <= 3:
        thisProject.Status = get_object_or_404(SubStatus, pk=projectStatus-1)
        thisProject.save()
        newLog = EventLog(Engagement=thisProject, By=request.user, Action="Downgraded the status to: " + str(thisProject.Status))
        newLog.save()
    return redirect(request.META['HTTP_REFERER'])

def ChangeProjectStauts(request, pk, status):
    thisProject = get_object_or_404(SubProject, pk=pk)
    thisProject.Status = GetSubStatus(status) 
    thisProject.save()
    newLog = EventLog(Engagement=thisProject, By=request.user, Action="Changed the status to: " + str(thisProject.Status))
    newLog.save()
    return redirect(request.META['HTTP_REFERER'])
