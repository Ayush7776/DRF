from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.InfoGeneric.as_view()),
    path('<int:id>',views.InfoGeneric2.as_view()),
]
