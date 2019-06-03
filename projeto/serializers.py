from rest_framework import serializers

from django.contrib.auth.models import User
from app.models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')
