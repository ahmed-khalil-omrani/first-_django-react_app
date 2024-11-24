from django.shortcuts import render 
from rest_framework import viewsets
from .serializers import DonnorSerializers , User
from .models import BloodDonnor
"""def index(request):
    return render(request,'index.html')"""
class DonnorView(viewsets.ModelViewSet):
    serializer_class=DonnorSerializers
    queryset=BloodDonnor.objects.all()

# Create your views here.
