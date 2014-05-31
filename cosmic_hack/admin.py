from django.contrib import admin
from cosmic_hack.models import Child, NumericalQuestion, NumericalQuestionAnswer;



class ChildAdmin(models.ModelAdmin):
	list_display = ("id", "name", "age");
admin.site.register(Child, ChildAdmin);