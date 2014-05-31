import json;
from django.http import HttpResponse, Http404, HttpResponseRedirect;
from cosmic_hack.models import NumericalQuestion, QuestionOrder, NUMERICAL_TYPE, PICTORIAL_TYPE, NumericalQuestionAnswer, Child;
from django.shortcuts import render;
from django.views.generic.base import View;
from django.utils.decorators import method_decorator;




def getAnonymousChild():
	return Child.objects.get(id = 1);



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
				questionDictionary["type"] = questionOrderRow.type;
				questions.append(questionDictionary);

		return questions;



# @returnHttpJson
def postNumericalQuestionAnswer(request):
	print("Hello");
	# return {"result": "ok"};
	return HttpResponse("Plain text", content_type = "text/plain");



# class PostNumericalQuestionAnswer(View):
# 	@method_decorator(returnHttpJson)
# 	def post(self, request):
# 		# print("Hello!");
# 		# print(request);

# 		# question = request.POST["question"];
# 		# answer = request.POST["answer"];
# 		# child = None;

# 		# print(question);
# 		# print(answer);

# 		# try:
# 		# 	childId = request.POST["child"];
# 		# 	try:
# 		# 		child = Child.objects.get(id = childId);
# 		# 	except (Child.DoesNotExist):
# 		# 		raise Http404;
# 		# except:
# 		# 	child = getAnonymousChild();

# 		# NumericalQuestionAnswer.objects.create(question = question, answer = answer, child = child);

# 		return {"result": "ok"};



class AddChild(View):
	@method_decorator(returnHttpJson)
	def post(self, request):
		isAnonymous = request.POST["isAnonymous"];

		child = None;

		if (isAnonymous):
			child = Child.objects.get(id = 1);
		else:
			name = request.POST["name"];
			age = request.POST["age"];
			child = Child.objects.create(name, age);

		return {"child": child.toDictionary()};



class GetChild(View):
	@method_decorator(returnHttpJson)
	def get(self, request, id):
		child = None;
		try:
			child = getAnonymousChild();
		except (Child.DoesNotExist):
			raise Http404;
		return {"child": child.toDictionary()};
