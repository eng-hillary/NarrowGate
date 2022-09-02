
from django.db import models
from django.contrib.auth.models import User
from common.models import Subject

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    employee_number = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to="images")
    home_phone = models.CharField(max_length=100, verbose_name="Home Phone")
    is_teacher = models.BooleanField(default=False)
    is_bursar = models.BooleanField(default=False)
    is_class_teacher = models.BooleanField(default=False)
    subjects = models.ManyToManyField(Subject, verbose_name='Subjects Taught',blank=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'.format()


