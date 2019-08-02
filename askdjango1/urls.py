"""askdjango1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path


urlpatterns = [
    path('', lambda r: redirect('blog:post_list'), name='root'),
    # 단순 리다이렉션에는 람다 활용하자!
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('dojo/', include(('dojo.urls', 'dojo'), namespace='dojo')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings. MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 개발환경에서 미디어 파일 서빙은? 스태틱 파일과는 다르게 서빙 미지원
# 개발 편의성 목적으로 직접 서빙 룰 추가 가능
# url 리퀘스트 있을때 스태틱에서 파일 찾아서 알아서 서빙을 하겠수다 +=

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]