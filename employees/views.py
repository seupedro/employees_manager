from django.shortcuts import render

import employees
from employees.models import Employee


def home(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})