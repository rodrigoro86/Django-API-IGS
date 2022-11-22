from django.contrib import admin
from software_manager.models import (
    Department, 
    Employee
)

class Departments(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 30

admin.site.register(Department, Departments)

class Employees(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 30

admin.site.register(Employee, Employees)