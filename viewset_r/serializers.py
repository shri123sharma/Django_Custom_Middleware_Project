from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields="__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields="__all__"

   