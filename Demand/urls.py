from django.conf.urls import url
from views import  DemandCreateView, DemandListView

app_name = 'Demand'

urlpatterns = [
    url(r'^$', DemandListView.as_view(), name="Index"),
    url(r'^Create/', DemandCreateView.as_view(), name="Create")

]

