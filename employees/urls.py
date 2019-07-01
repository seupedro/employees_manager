from django.urls import path

from employees.views import home_employees_list

urlpatterns = [
    path('', home_employees_list),
]
