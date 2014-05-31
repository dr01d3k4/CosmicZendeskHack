from django.shortcuts import render;
from django.views.generic.base import View;



class Index(View):
	def get(self, request):
		context = { };
		return render(request, "www/index.html", context);