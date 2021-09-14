from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import home
from home import views
urlpatterns = [
    url(r'^$',home.views.home,name='home'),
    url(r'^login/$',home.views.login,name='login'),
    url(r'^logout/$',home.views.logout,name='logout'),
    url(r'^register/$',home.views.register,name='register'),
]
