from django.contrib import admin
from cosmic_hack.models import Child, NumericalQuestion, NumericalQuestionAnswer, QuestionOrder;



class ChildAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "age");

	class Meta(object):
		verbose_name_plural = "Children";

admin.site.register(Child, ChildAdmin);




class NumericalQuestionAdmin(admin.ModelAdmin):
	list_display = ("id", "question");

admin.site.register(NumericalQuestion, NumericalQuestionAdmin);



class NumericalQuestionAnswerAdmin(admin.ModelAdmin):
	list_display = ("id", "child", "answer");

admin.site.register(NumericalQuestionAnswer, NumericalQuestionAnswerAdmin);



class QuestionOrderAdmin(admin.ModelAdmin):
	list_display = ("id", "type", "order", "question_number");
	
admin.site.register(QuestionOrder, QuestionOrderAdmin);