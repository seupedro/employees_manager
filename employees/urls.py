from django.urls import path

from employees.views import home

urlpatterns = [
    path('', home),
]
