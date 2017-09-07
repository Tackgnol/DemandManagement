from django.contrib import admin
from Demand.models import Activity, BusinessPriority, Category, Country, Project, Region, Risk, Status, UserAssosiation

# Register your models here.

admin.site.register(Activity)
admin.site.register(BusinessPriority)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Project)
admin.site.register(Region)
admin.site.register(Risk)
admin.site.register(Status)
admin.site.register(UserAssosiation)
