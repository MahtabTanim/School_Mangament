from django.urls import path
from django.contrib import admin
from school_site import views


urlpatterns = [
    path('homepage/',views.home_page,name='home_page'),
    path('about/',views.about_page,name='about_page'),
    path('contact/',views.contact_page,name='contact_page'),
]