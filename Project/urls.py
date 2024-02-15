
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
]
