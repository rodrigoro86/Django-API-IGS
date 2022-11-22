from rest_framework import serializers
from software_manager.models import Department, Employee
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department']

    def validate_email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise serializers.ValidationError('email is invalid')    
        return email
