from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create_note),
    url(r'^delete/(?P<id>\d+)$', views.delete_note),
    
]
