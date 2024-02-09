from rest_framework import serializers
from .models import *
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