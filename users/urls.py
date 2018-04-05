"""Defines URL patterns for users"""
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
	
	# Login page
	# users/login/
	url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),

	# Logout page
	# users/logout/
	url(r'^logout/$', views.logout_view, name='logout'),


]