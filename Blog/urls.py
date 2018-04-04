from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	
	# /admin/
    url(r'^admin/', admin.site.urls),

    # 
    url(r'', include('blogs.urls', namespace='blogs')),


]
