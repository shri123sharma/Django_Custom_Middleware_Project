from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status 
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import *

# Create your views here.
class UserViewSet(ViewSet):
    queryset=User.objects.all()

    def list(self,request):
        serializer=UserSerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        user_data=get_object_or_404(self.queryset,pk=pk)
        serializer=UserSerializer(user_data)
        return Response(serializer.data)
    
    def create(self,request,pk):
       user_data=UserSerializer(data=request.data)
       if user_data.is_valid():
           user_data.save()
           return Response("data is valid")
       else:
           return Response("data is not valid")
    
class CompanyViewSet(ViewSet):
    def list(self,request):
        company=Company.objects.all()
        serializer=CompanySerializer(company,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
          company=Company.objects.get(id=id)
          serializer=CompanySerializer(company)
          return Response(serializer.data)
    
    def create(self,request):
        serializer=CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

            
    def destroy(self,request,pk=None):
        id=pk
        if id is not None:
            company=Company.objects.get(id=id)
            serializer=CompanySerializer(company)
            return Response(serializer.data)
        

class EmployeeViewSet(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    

class CityViewSet(ReadOnlyModelViewSet):
    serializer_class=CitySerializer
    queryset=City.objects.all()

class AccountViewset(ModelViewSet):
    serializer_class=AccountSerializer
    
    def get_queryset(self):
        return Account.objects.all()

    

       

        