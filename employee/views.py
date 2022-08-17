from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin


class MyOwnViewSet(GenericViewSet, RetrieveModelMixin, DestroyModelMixin):
    pass


class EmployeeOperations(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
