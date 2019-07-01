from rest_framework import serializers

from employees.models import Employee


# Serializers define the API representation.
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'department')

