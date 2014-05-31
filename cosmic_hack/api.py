import json;
from django.http import HttpResponse, Http404, HttpResponseRedirect;
from cosmic_hack.models import NumericalQuestion;



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

		jsonString = json.dumps(jsonObject);
		return HttpResponse(jsonString, content_type = "application/json");

	return innerFunction;




@returnHttpJson
def getQuestions(request):
	return [question.toDictionary() for question in NumericalQuestion.objects.all()];