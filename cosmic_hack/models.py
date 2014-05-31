from django.db import models;



class Child(models.Model):
	name = models.CharField(max_length = 256);
	age = models.IntegerField();

	def toDictionary(self):
		return {
			"name": self.name,
			"age": self.age,
			"id": self.id
		};

	def __unicode__(self):
		return "%s: %d" % (self.name, self.age);

	class Meta(object):
		verbose_name_plural = "Children";



class NumericalQuestion(models.Model):
	question = models.CharField(max_length = 200);

	def toDictionary(self):
		return {
			"id": self.id,
			"question": self.question
		};


	def __unicode__(self):
		return self.question;



class NumericalQuestionAnswer(models.Model):
	child = models.ForeignKey("Child");
	question = models.ForeignKey("NumericalQuestion");
	answer = models.IntegerField();



NUMERICAL_TYPE = "NUM";
PICTORIAL_TYPE = "PIC";

QUESTION_TYPE_CHOICE = (
	(NUMERICAL_TYPE, "Numerical"),
	(PICTORIAL_TYPE, "Pictorial")
);

class QuestionOrder(models.Model):
	type = models.CharField(max_length = 3, choices = QUESTION_TYPE_CHOICE, default = NUMERICAL_TYPE);
	order = models.IntegerField(unique = True);
	question_number = models.IntegerField();

	def __unicode__(self):
		return "%s %d %d" % (self.type, self.order, self.question_number);