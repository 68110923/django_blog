from django.contrib import admin
from django.urls import path,re_path
from blogapp.views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('user/post/', userpost, name='userpost'),
    path('user/get/', userget, name='userget'),
    path('user/put/', userput, name='userput'),
    path('user/', user, name='user'),

    path('article/', article, name='article'),
    path('article/post/', articlepost, name='articlepost'),

    re_path('comment/articleID=\d*',article_comment,name='article_comment')
]