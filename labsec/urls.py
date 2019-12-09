#Django
from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler400, handler500

handler404 = 'website.views.handler404'
handler500 = 'website.views.handler500'

urlpatterns = [
    path('', include('website.urls', namespace='website')),
    path('admin/', admin.site.urls),
]
