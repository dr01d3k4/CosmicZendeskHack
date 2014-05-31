from django.contrib import admin
from cosmic_hack.models import Child, NumericalQuestion, NumericalQuestionAnswer;



class ChildAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "age");
admin.site.register(Child, ChildAdmin);




class NumericalQuestionAdmin(admin.ModelAdmin):
	list_display = ("id", "question");
admin.site.register(NumericalQuestion, NumericalQuestionAdmin);



class NumericalQuestionAnswerAdmin(admin.ModelAdmin):
	list_display = ("id", "child");
admin.site.register(NumericalQuestionAnswer, NumericalQuestionAnswerAdmin);