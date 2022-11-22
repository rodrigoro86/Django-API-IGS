from rest_framework.test import APITestCase
from rest_framework import status
import json
from django.urls import reverse
from django.contrib.auth.models import User
from software_manager.models import (
    Employee, 
    Department
)

class URLDeparmentTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='test', password='test')
        self.client.force_authenticate(user)
        self.list_url = reverse('Departments-list')

        Department.objects.create(
            name='Department_A'
        )
    
    def test_get_all_departments(self):
        """GET all departments data and check status HTTP_200_OK"""
        response = self.client.get(self.list_url)
        department = Department.objects.get(id=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg='Status differnt HTTP_200_OK')
        self.assertEqual(department.name, response.json()[0]['name'], msg='Value department name differnt of value get')
        
    def test_post_new_department_create(self):
        """POST new department and validate value"""
        new_department = {
            'name': 'kitchen'
        }
        response = self.client.post(self.list_url, data=json.dumps(new_department), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = self.client.get(self.list_url)
        department = Department.objects.get(id=2)
        self.assertEqual(department.name, response.json()[1]['name'], msg='Value new department name differnt of value get')
    
    def test_remove_department(self):
        """DELETE department"""

        response = self.client.delete(self.list_url+'1')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_put_department(self):
        """PUT change department name"""
        new_department = {
            'name': 'kitchen'
        }
        response = self.client.put(self.list_url + '1', data=json.dumps(new_department), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        
        response = self.client.get(self.list_url)
        department = Department.objects.get(id=1)
        self.assertEqual(department.name, response.json()[0]['name'], msg='Value new department name differnt of value get')
    
class URLEmployeeTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='test', password='test')
        self.client.force_authenticate(user)
        self.list_url = reverse('Employees-list')

        self.department = Department.objects.create(
            name='kitchen'
        )
        Employee.objects.create(
            name='SpongeBob Squarepants',
            email='spongebob@krustykrab.com.br',
            department=self.department
        )
    
    def test_get_all_employee(self):
        """GET all departments data and check status HTTP_200_OK"""
        response = self.client.get(self.list_url)
        employee = Employee.objects.get(id=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg='Status differnt HTTP_200_OK')
        self.assertEqual(employee.name, response.json()[0]['name'], msg='Value employee name differnt of value get')
        self.assertEqual(employee.email, response.json()[0]['email'], msg='Value employee email differnt of value get')
        self.assertEqual(employee.department.id, response.json()[0]['department'], msg='Value employee deparmentId differnt of value get')
        
    def test_post_new_employee_create(self):
        """POST new employee and validate value"""
        new_employee = {
            'name': 'Patrick',
            'email':'patrick@krustykrab.com.br',
            'department': 1,
        }
        response = self.client.post(self.list_url, data=json.dumps(new_employee), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = self.client.get(self.list_url)
        employee = Employee.objects.get(id=2)
        self.assertEqual(employee.name, response.json()[1]['name'], msg='Value new employee name differnt of value get')
        self.assertEqual(employee.email, response.json()[1]['email'], msg='Value new employee email differnt of value get')
        self.assertEqual(employee.department.id, response.json()[1]['department'], msg='Value new employee department differnt of value get')
        
    def test_remove_employee(self):
        """DELETE employee"""

        response = self.client.delete(self.list_url+'1')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
    
    def test_put_employee(self):
        """PUT change department name"""
        new_employee = {
            'name': 'Mr. Krabs',
            'email':'mrkrabs@krustykrab.com.br',
            'department': 1,
        }
        response = self.client.put(self.list_url + '1', data=json.dumps(new_employee), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        
        response = self.client.get(self.list_url)
        employee = Employee.objects.get(id=1)
    
        self.assertEqual(employee.name, response.json()[0]['name'], msg='Value new employee name differnt of value get')
        self.assertEqual(employee.email, response.json()[0]['email'], msg='Value new employee email differnt of value get')
        self.assertEqual(employee.department.id, response.json()[0]['department'], msg='Value new employee department differnt of value get')
        