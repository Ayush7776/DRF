from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.hello),
    path('post',views.hi),
    path('update/<id>',views.update),
    path('miniupdate/<id>',views.miniupdate),
    path('remove/<id>',views.remove),
]
