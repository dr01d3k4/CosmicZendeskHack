from django.conf.urls import patterns, include, url;
from cosmic_hack import views, api;



urlpatterns = patterns("",
	url(r"^$", views.Index.as_view(), name = "index"),

	url(r"^get-all-questions/$", api.GetAllQuestions.as_view(), name = "get-all-questions"),
	url(r"^post-numerical-question-answer/$", api.PostNumericalQuestionAnswer.as_view(), name = "post-numerical-question-answer")
);