from tabnanny import verbose
from django.db import models
import datetime


# class Stream(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Stream Name")

#     def __str__(self):
#         return self.name

class Class(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    def __str__(self):
        return self.name

class Subject(models.Model):
    code = models.CharField(max_length=100, unique=True, blank=False, verbose_name="Subject Code")
    name = models.CharField(max_length=100, verbose_name="Subject Name")
    class_taught  = models.OneToOneField(Class, on_delete=models.SET_NULL, null=True, verbose_name="Class Taught" )

    def __str__(self):
        return f'{self.name}'.format()


class Term(models.Model):
    """
    This model represents a given study term in a year
    """
    STATUSES = (
        ('current', 'Current'),
        ('previous', 'Previous'),
        ('next', 'Next')
    )

    TERMS = (
        ('ft', 'First Term'),
        ('st', 'Second Tern'),
        ('tt', 'Third Term')
    )
    name = models.CharField(max_length=100,choices=TERMS, verbose_name="Term Name")
    status = models.CharField(max_length=100, choices=STATUSES, default='previous')
    start_date = models.DateField(default=datetime.datetime.today)
    end_date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return f'{self.name} {self.start_date}'.format()

