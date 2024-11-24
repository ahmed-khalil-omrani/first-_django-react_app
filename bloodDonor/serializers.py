from rest_framework import serializers
from .models import BloodDonnor
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
class DonnorSerializers(serializers.ModelSerializer):
    user=UserSerializers()
    class Meta:
        model=BloodDonnor
        fields='__all__'
    def create(self,validated_data):
        user_data=validated_data.pop('user')
        user=User.objects.create(**user_data)
        blood_donor=BloodDonnor.objects.create(user=user,**validated_data)
        return blood_donor
