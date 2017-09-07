from django.conf.urls import url
from views import NewQuestion, AllQuestions, ViewQuestion, UpdateQuestion, NewSurvey, FillSurvey, AllSurveys
app_name = 'Survey'

urlpatterns = [
    url(r'^$', AllSurveys.as_view(), name='Index'),
    url(r'^Create/$', NewQuestion.as_view(), name="Create"),
    url(r'^Questions/$', AllQuestions.as_view(), name='Questions'),
    url(r'^Question/(?P<pk>\d+)/$', ViewQuestion.as_view(), name='Details'),
    url(r'^Update/(?P<pk>\d+)/$',  UpdateQuestion.as_view(), name='Edit'),
    url(r'^NewSurvey/$', NewSurvey.as_view(), name='NewSurvey'),
    url(r'^Survey/(?P<pk>\d+)/$',  FillSurvey.as_view(), name='Survey'), 
]

