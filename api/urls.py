from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.InfoApiView.as_view()),
    path('register',views.Register.as_view())
]
