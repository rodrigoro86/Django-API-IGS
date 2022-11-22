from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters, generics
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from software_manager.models import Department, Employee
from software_manager.serializer import DepartmentSerializer, EmployeeSerializer

class DepartmentsViewSet(viewsets.ModelViewSet):
    """List all data of Departaments"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

class EmployeesViewSet(viewsets.ModelViewSet):
    """List all data of Employees"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

class ListEmployeesByDepartmentViewSet(generics.ListAPIView):
    """Filter Employees by DepartmentId"""
    def get_queryset(self):
        queryset = Employee.objects.filter(department=self.kwargs['department'])
        return queryset
    
    serializer_class = EmployeeSerializer