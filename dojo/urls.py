from . import views
from django.urls import re_path, path

urlpatterns = [
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    re_path(r'^hello/(?P<name>[r-힣]+)/(?P<age>\d+)/$', views.hello),
    path('list1/', views.post_list1),
    path('list2/', views.post_list2),
    path('list3/', views.post_list3),
    path('excel/', views.excel_download),
]