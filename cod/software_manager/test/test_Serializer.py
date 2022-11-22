from django.test import TestCase
from software_manager.models import (
    Employee, 
    Department
)
from software_manager.serializer import (
    EmployeeSerializer,
    DepartmentSerializer
)

class DepartmentSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.department_test = Department(
            name='Department_A'
        )
        self.serializer = DepartmentSerializer(instance=self.department_test)

    def test_validate_fields_serializers(self):
        """Validate fields Department Serializers"""
        department_data = self.serializer.data
        self.assertEqual(set(department_data.keys()), set(['id','name']), msg='DepartmentSerializer fields differnt of [id, name]') 
    
    def test_validate_values_modelTest_equal_DeparmentSerializer(self):
        """Validate values department_test with values DeparmentSerializer"""
        department_data = self.serializer.data
        self.assertEqual(department_data['name'], self.department_test.name, msg='Value department_teste name different of department Serialized') 

class EmployeeSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.department = Department.objects.create(
            name='kitchen'
        )
        self.employee_test = Employee(
            name='SpongeBob Squarepants',
            email='spongebob@krustykrab.com.br',
            department=self.department
        )

        self.serializer = EmployeeSerializer(instance=self.employee_test)

    def test_validate_fields_serializers(self):
        """Validate fields Employee Serializers"""
        employee_data = self.serializer.data
        self.assertEqual(set(employee_data.keys()), set(['id','name', 'email', 'department']),
             msg="DepartmentSerializer fields differnt of ['id','name', 'email', 'department']") 
    
    def test_validate_values_modelTest_equal_EmployeeSerializer(self):
        """Validate values employee_test with values EmployeeSerializer"""
        employee_data = self.serializer.data
        self.assertEqual(employee_data['name'], self.employee_test.name, msg='Value employee_data name different of employee Serialized')
        self.assertEqual(employee_data['email'], self.employee_test.email, msg='Value employee_data email different of employee Serialized') 
        self.assertEqual(employee_data['department'], self.employee_test.department.id, msg='Value employee_data department different of employee Serialized') 

    def test_validate_email_text(self):
        employee_test_2 = Employee(
            name='SpongeBob Squarepants',
            email='value_wrong',
            department=self.department
        )

        serializer = EmployeeSerializer(data=employee_test_2)
        self.assertEqual(serializer.is_valid(), False, msg='Employee email accept format wrong')