from django.db import models;



class Child(models.Model):
	name = models.CharField(max_length = 256);
	age = models.IntegerField();



	def __unicode__(self):
		return "%s: %d" % (self.name, self.age);




class NumericalQuestion(models.Model):
	question = models.CharField(max_length = 200);



	def toDictionary(self):
		return {
			"id": self.id,
			"question": self.question
		};




class NumericalQuestionAnswer(models.Model):
	child = models.ForeignKey("Child");