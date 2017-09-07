from django.contrib import admin
from Engagement.models import SubProject, SetArea, Step, RequestType, Complexity, SubStatus, ProjectManagement
# Register your models here.
admin.site.register(SubProject)
admin.site.register(SetArea)
admin.site.register(Step)
admin.site.register(RequestType)
admin.site.register(Complexity)
admin.site.register(SubStatus)
admin.site.register(ProjectManagement)

