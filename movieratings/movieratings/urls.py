"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app1.views import AccountProfile

urlpatterns = [
    url(r'^logout/', 'django.contrib.auth.views.logout',
        {'next_page':"/app1/list_movies"}, name='logout'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^app1/', include('app1.urls')),
    url(r'^accounts/profile/', login_required(AccountProfile.as_view()),
        name='account_profile'),
    url(r'^admin/', include(admin.site.urls)),
]
