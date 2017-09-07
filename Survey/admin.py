from django.contrib import admin
from models import Question, Section, Answer, InputType, Option, QuestionSet, Survey, Unit, OptionGroup


# Register your models here.
admin.site.register(Question)
admin.site.register(Section)
admin.site.register(Answer)
admin.site.register(InputType)
admin.site.register(Option)
admin.site.register(QuestionSet)
admin.site.register(Unit)
admin.site.register(OptionGroup)
admin.site.register(Survey)