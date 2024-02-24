from rest_framework import serializers
from .models import *


from django.contrib.auth.models import User

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Info
        # fields=['id','Name','City']
        # exclude=['id']
        fields='__all__'