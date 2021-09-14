from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import student
from student import views
urlpatterns = [
    url(r'^$',student.views.student_detail,name='student_detail'),
    url(r'^Manage_student/$',student.views.addStudent,name='add_student'),
    url(r'^student/(?P<std>[0-9]+)/$',student.views.standard,name='standard'),
    url(r'^student_mark/(?P<std>[0-9]+)/$',student.views.entermarks,name='entermark'),
    url(r'^student_graph/(?P<std>[0-9]+)/(?P<student_id>[0-9]+)/$', student.views.student_graph, name='student_graph'),
    url(r'^report/(?P<std>[0-9]+)/$', student.views.report, name='report'),
    url(r'^detail_report/(?P<std>[0-9]+)/(?P<student_id>[0-9]+)/$', student.views.detail_report, name='detail_report'),
    url(r'^rank/(?P<std>[0-9]+)/(?P<student_id>[0-9]+)/$', student.views.rank, name='rank'),
    url(r'^rank_graph/(?P<std>[0-9]+)/(?P<student_id>[0-9]+)/$', student.views.rank_graph, name='rank_graph'),
]