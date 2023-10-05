from django.db import models


class Users(models.Model):
   Firstname = models.CharField(max_length=80)
   Middlename = models.CharField(max_length=80)
   Lastname = models.CharField(max_length=80)
   Email= models.EmailField(max_length=80)
