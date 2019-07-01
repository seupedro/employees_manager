from django.shortcuts import render
from rest_framework import viewsets

from employees.models import Employee
from employees.serializers import EmployeeSerializer


def home_employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})


# ViewSets define the view behavior.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
