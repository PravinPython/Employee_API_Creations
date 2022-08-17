from rest_framework.serializers import ModelSerializer
from employee.models import Employee
# from rest_framework import serializers


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        # include =('id','name','age')
        # exclude = ('id', 'name', 'age')
