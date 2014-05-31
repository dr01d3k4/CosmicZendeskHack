from django.conf.urls import patterns, include, url;
from cosmic_hack import views, api;



urlpatterns = patterns("",
	url(r"^$", views.Index.as_view(), name = "index"),

	url(r"^get-all-questions/$", api.GetAllQuestions.as_view()),
	url(r"^post-numerical-question-answer/$", api.postNumericalQuestionAnswer),
	url(r"^add-child/$", api.AddChild.as_view()),
	url(r"^get-child/(?P<id>\d+)/$", api.GetChild.as_view())
);