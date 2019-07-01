from django.db import models


class Employee(models.Model):

    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, max_length=50)

    DEPARTMENTS = [
        ('RH', 'Human Resources'),
        ('ADM', 'Administration'),
        ('DEV', 'Development'),
        ('IT', 'Information Technology'),
    ]
    department = models.CharField(blank=False, max_length=100, choices=DEPARTMENTS)

    def __str__(self):
        return self.name
