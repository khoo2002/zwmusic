from django.urls import path, include

from django.conf.urls import url

from convert import views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

from convert.views import *


urlpatterns = [
    url(r'^$', views.index),
    url(r'^index$', views.index),
    url(r'^converter$', views.converter),
    url(r'^mp4tomp3$', views.mp4tomp3),
    path('readydl', views.readydl),
    path('readydl/<dlfile>/<file>',views.download),
    path('index/<dlfile>/<file>',views.indexdownload),
    path('mp4tomp3/<dlfile>/<file>', views.download),
    path('index/<dlfile>/<file>',views.download),
    path('index/<imgnfile>',views.picture),
    path('invest',views.invest),
    path('dlqrcode',views.dlqrcode),
    path('<filename>',views.stream_http)
    ]
