from django.test import TestCase
from software_manager.models import (
    Employee, 
    Department
)

class DepartmentTestCase(TestCase):
    def setUp(self) -> None:
        Department.objects.create(
            name='Department_A'
        )
    
    def test_validateAtributsDepartmentModel(self):
        """Validate name of atributes Department Model"""
        department = Department.objects.get(id=1)
        self.assertEquals(department._meta.get_field('name').verbose_name, 'name', msg='Atribute name not exist')
    
    def test_lengh_atributes(self):
        """Validate max_length atribute name"""
        department = Department.objects.get(id=1)
        self.assertEquals(department._meta.get_field('name').max_length, 30, msg='max_length name different to 30 characters')

class EmployeeTestCase(TestCase):
    def setUp(self) -> None:
        department = Department.objects.create(
            name='kitchen'
        )
        Employee.objects.create(
            name='SpongeBob Squarepants',
            email='spongebob@krustykrab.com.br',
            department=department
        )

    def test_validateAtributsDepartmentModel(self):
        """Validate name of atributes Employee Model"""
        employee = Employee.objects.get(id=1)
        self.assertEquals(employee._meta.get_field('name').verbose_name, 'name', msg='Atribute name not exist')
        self.assertEquals(employee._meta.get_field('email').verbose_name, 'email', msg='Atribute name not exist')
        self.assertEquals(employee._meta.get_field('department').verbose_name, 'department', msg='Atribute name not exist')
    
    def test_lengh_atributes(self):
        """Validate max_length atribute name"""
        employee = Employee.objects.get(id=1)
        self.assertEquals(employee._meta.get_field('name').max_length, 30, msg='max_length name different to 30 characters')
        self.assertEquals(employee._meta.get_field('email').max_length, 50, msg='max_length name different to 50 characters')