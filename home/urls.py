from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('blog/',blog,name='blog'),
    path('b1/',b1,name='b1'),
    path('b2/',b2,name='b2'),
    path('b3/',b3,name='b3'),
]
