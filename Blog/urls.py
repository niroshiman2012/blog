from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	
	# /admin/
    url(r'^admin/', admin.site.urls),

    # /users/
	url(r'^users/', include('users.urls', namespace='users')),
    # / 
    url(r'', include('blogs.urls', namespace='blogs')),



]
