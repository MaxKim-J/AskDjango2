from . import views
from django.urls import re_path

urlpatterns = [
re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum)
]