import json;
from django.http import HttpResponse, Http404, HttpResponseRedirect;
from cosmic_hack.models import NumericalQuestion, QuestionOrder, NUMERICAL_TYPE, PICTORIAL_TYPE, NumericalQuestionAnswer;
from django.views.generic.base import View;
from django.utils.decorators import method_decorator;



def isInteger(x):
	return isinstance(x, (int, long));



def toInteger(x):
	try:
		val = int(x);
		return val;
	except ValueError:
		return None;



def returnHttpJson(viewFunction):
	def innerFunction(*args, **kwargs):
		jsonObject = viewFunction(*args, **kwargs);

		if (isInteger(jsonObject)):
			return HttpResponseRedirect("/");

		jsonString = json.dumps(jsonObject, indent = 4);
		return HttpResponse(jsonString, content_type = "application/json");

	return innerFunction;




class GetAllQuestions(View):
	@method_decorator(returnHttpJson)
	def get(self, request):
		questionOrder = QuestionOrder.objects.all().order_by("order");

		questions = [ ];

		for questionOrderRow in questionOrder:
			question = None;

			if (questionOrderRow.type == NUMERICAL_TYPE):
				question = NumericalQuestion.objects.get(id = questionOrderRow.question_number);

	 		# elif (questionOrderRow.type == PICTORIAL_TYPE):
				# question = Picture.objects.get(id = questionOrderRow.question_number);

			if (question is not None):
				questionDictionary = question.toDictionary();
				questionDictionary["order"] = questionOrderRow.order;
				questions.append(questionDictionary);

		return questions;



class PostNumericalQuestionAnswer(View):
	@method_decorator(returnHttpJson)
	def post(self, request):
		question = request.POST["question"];
		answer = request.POST["answer"];
		child = None;

		try:
			child = request.POST["child"];
		except:
			pass;


		if (child is not None):
			NumericalQuestionAnswer.objects.create(question = question, answer = answer, child = child);
		else:
			NumericalQuestionAnswer.objects.create(question = question, answer = answer);

		return {"result": "ok"};