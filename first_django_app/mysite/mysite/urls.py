"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# from django.conf.urls import include, url
# from django.contrib import admin

# urlpatterns = [
#     path(r'^polls/', include('polls.urls')),
#     path(r'^admin/', admin.site.urls),
# ]

# Django 4.0에서 django.conf.urls.url() 함수는 제거되었습니다.
# 대신 django.urls.re_path() 함수를 사용하십시오. 정규표현식 기반 URL 패턴임
# 혹은, path() 함수를 사용하십시오. 경로 기반 URL 패턴임
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

