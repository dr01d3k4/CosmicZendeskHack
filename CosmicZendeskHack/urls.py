from django.conf.urls import patterns, include, url;



from django.contrib import admin;
admin.autodiscover();



urlpatterns = patterns("",
	url(r"^admin/", include(admin.site.urls)),
	url(r"^cosmic_hack/", include("cosmic_hack.urls", namespace = "cosmic_hack"))
);



import settings;
if (settings.DEBUG):
	urlpatterns += patterns("django.views.static", (r"media/(?P<path>.*)", "serve", {"document_root": settings.MEDIA_ROOT}), );