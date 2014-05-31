from django.conf.urls import patterns, include, url;
from cosmic_hack import views;



urlpatterns = patterns("",
	url(r"^$", views.Index.as_view(), name = "index"),
);