from rest_framework import serializers
from .models import *


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

    def create(self,validated_data):
        user= User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Info
        # fields=['id','Name','City']
        # exclude=['id']
        fields='__all__'

    def validate(self,data):
            if data['Age']<18:
                    raise serializers.ValidationError({'error':'Age Cannot Be less Than 18'})
            return data
            if data['Name']:
                    for i in data['Name']:
                        if i.isdigit():
                            raise serializers.ValidationError({'error':'Invalid Entry'})    
            return data