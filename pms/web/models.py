from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Student(models.Model):
    Username = models.OneToOneField(User, on_delete=models.CASCADE)
    PhoneNumber = PhoneNumberField()
    Avatar = models.ImageField(upload_to='web/static/avatar/', default='web/static/avatar/default.png')
    Name = models.CharField(max_length=30, blank=True)
    Family = models.CharField(max_length=30, blank=True)
    IsValid = models.BooleanField(default=False)

    def __str__(self):
        return "{}  {}".format(self.Name, self.Family)
