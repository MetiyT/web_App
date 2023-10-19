from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
   pass

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employee_code = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.employee_code
    
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in = models.DateTimeField(null=True)
    check_out = models.DateTimeField(null=True)

    