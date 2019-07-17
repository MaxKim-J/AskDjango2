from . import views
from django.urls import re_path

urlpatterns = [
   re_path(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
   re_path(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
   re_path(r'^sum/(?P<x>\d+)/$', views.mysum),
]