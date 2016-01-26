"""bringme_life URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from bring_me import views


urlpatterns = patterns('',
	# Registration of new users 
	url(r'^register/$', views.RegistrationView.as_view()), 
	# Todos endpoint 
	url(r'^todos/$', views.TodosView.as_view()), 
	url(r'^todos/(?P<todo_id>[0-9]*)$', views.TodosView.as_view()), 
	# API authentication 
	url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')), 
	url(r'^api-auth/', include('rest_framework.urls',\
	 namespace='rest_framework')),
)




