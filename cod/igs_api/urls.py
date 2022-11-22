from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from software_manager.views import (
    DepartmentsViewSet,
    EmployeesViewSet,
    ListEmployeesByDepartmentViewSet,
)

schema_view = get_schema_view(
    openapi.Info(
        title="API Software Manager IGS",
        default_version='v1',
        description="API manager Departments and Employees",
        terms_of_service="#",
        contact=openapi.Contact(email="rodrigoliveira132@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes = [permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('department', DepartmentsViewSet, basename="Departments")
router.register('employee', EmployeesViewSet, basename="Employees")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('employee/departmentId=<int:department>', ListEmployeesByDepartmentViewSet.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
