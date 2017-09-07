from django.conf.urls import url
from views import  SubProjectListView, SubProjectDetailView, SubProjectMyListView, NextStatus, PreviousStatus, SubProjectMyInactive, SubprojectActivate, ChangeProjectStauts
app_name = 'Engagement'

urlpatterns = [
    url(r'^$', SubProjectListView.as_view(), name="Index"),
    url(r'^MyEngagements/$', SubProjectMyListView.as_view(), name="MyProjects"),
    url(r'^(?P<pk>\d+)/$', SubProjectDetailView.as_view(), name='Detail'),
    url(r'^Inactive/$',  SubProjectMyInactive.as_view(), name='Inactive'),
    url(r'^Activate/(?P<pk>\d+)/$', SubprojectActivate.as_view(), name='Activate'),
    url(r'^NextStatus/(?P<pk>\d+)/$', NextStatus, name='NextStatus'),
    url(r'^PreviousStatus/(?P<pk>\d+)/$', PreviousStatus, name='PreviousStatus'),
    url(r'^ReactivateProject/(?P<pk>\d+)/(?P<status>[\w ]+)/$', ChangeProjectStauts, name='ChangeProject'),    
]

