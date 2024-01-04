from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('',views.index,name='home'),
    path('blogs',views.blogs,name='blogs'),
    path('blog/<str:val>',views.single,name='single')
    
]