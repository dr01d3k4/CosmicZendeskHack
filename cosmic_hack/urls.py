from django.conf.urls import patterns, include, url;
from cosmic_hack import views, api;



urlpatterns = patterns("",
	url(r"^$", views.Index.as_view(), name = "index"),

	url(r"^get-questions/$", api.getQuestions, name = "get-questions")
);