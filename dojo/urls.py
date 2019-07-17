from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    re_path(r'^hello/(?P<name>[r-힣]+)/(?P<age>\d+)/$', views.hello)
]