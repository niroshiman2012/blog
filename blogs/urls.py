"""Contains url patterns for blogs."""

from django.conf.urls import url

from . import views

urlpatterns = [
	
    # Homepage
    # /
    url(r'^$', views.index, name='index'),

    # Detail page for post
    # /post/id
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),

    # Page for adding a new post
    # /new_post/
	url(r'^new_post/$', views.new_post, name='new_post'),

	# Page for editing a post
	# /edit_post/id
	url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
]
