from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_jalali.db import models as jmodels

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


class Course(models.Model) :
    Name = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return "{}".format(self.Name)


class Todo(models.Model):
    objects = jmodels.jManager()
    StudentName = models.OneToOneField(Student, on_delete=models.CASCADE)
    DueDate = jmodels.jDateField()
    CourseName = models.ForeignKey(Course, on_delete=models.CASCADE)
    StudyHour = models.IntegerField(blank=True)
    TestNumber = models.IntegerField(blank=True)

    def __str__(self):
        return "{} : {}".format(self.StudentName, self.CourseName)


class Done(models.Model):
    objects = jmodels.jManager()
    StudentName = models.OneToOneField(Student, on_delete=models.CASCADE)
    DoneDate = jmodels.jDateField()
    CourseName = models.OneToOneField(Course, on_delete=models.CASCADE)
    StudyHour = models.IntegerField(blank=True)
    TestNumber = models.IntegerField(blank=True)

    def __str__(self):
        return "{} : {}".format(self.StudentName, self.CourseName)

