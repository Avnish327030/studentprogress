from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import exam
from exam import views
urlpatterns = [
    url(r'^$',exam.views.home,name='exam'),
]
