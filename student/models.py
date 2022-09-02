from django.urls import reverse
from django.db import models
from employee.models import Subject
from common.models import Class, Term



class Circumstance(models.Model):
    CURCUMSTANCES = (
        ('deaf', 'Deaf'),
        ('lame', 'Lame'),
        ('blind', 'Blind'),
        ('others', 'Others')
    )
    name = models.CharField(max_length=100,choices=CURCUMSTANCES, verbose_name="First Name")
    description = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    student_number = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="images", null=True, blank=True, default='images/default.jpeg', verbose_name='Photo')
    circumstances = models.ManyToManyField(Circumstance, verbose_name="Special Circumstances")
    current_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, verbose_name="Current Class")
    current_term = models.ForeignKey(Term, on_delete=models.SET_NULL, null=True, verbose_name="Current Term")
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name="Home Address")
    phone = models.CharField(max_length=100,  null=True, blank=True,verbose_name="Home Phone")

    #guardian information
    guardian_first = models.CharField(max_length=100, null=True,blank=True,verbose_name="Gurdaine First Name")
    guardian_last = models.CharField(max_length=100, null=True,blank=True,verbose_name="Guardian Last Name")
    relationship = models.CharField(max_length=100, null=True,blank=True,verbose_name="Realtionship")
    guardian_occupation = models.CharField(max_length=100, null=True,blank=True,verbose_name="Guardian Occupation")
    guardian_phone = models.CharField(max_length=100, null=True,blank=True,verbose_name="Guardian Phone")
    guardian_email = models.EmailField(max_length=100, null=True,blank=True,verbose_name="Guardian Email")
    guardian_address = models.CharField(max_length=100, null=True,blank=True,verbose_name="Guardian Address")

    def get_absolute_url(self):
        return reverse('student:student-detail', kwargs={'pk': self.pk})


    def __str__(self):
        return f'{self.first_name} {self.last_name}'.format()

    

# class Guardian(models.Model):
#     guardian_number = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=100, verbose_name="First Name")
#     last_name = models.CharField(max_length=100, verbose_name="Last Name")
#     occupation = models.CharField(max_length=100, verbose_name="Occupation")
#     photo = models.ImageField(upload_to="images", null=True, blank=True)
#     home_phone = models.CharField(max_length=100, verbose_name="Home Phone")
#     email = models.EmailField(max_length=100, verbose_name="Email Address")

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'.format()


# class StudentGuardians(models.Model):
#     RELATIONSHIPS = (
#         ('father', 'Father'),
#         ('mother', 'MOther'),
#         ('brother', 'Brother'),
#         ('sister', 'Sister'),
#         ('uncle', 'Uncle'),
#         ('aunt', 'Aunt'),
#     )
#     Student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     Guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
#     relationship = models.CharField(max_length=100, choices=RELATIONSHIPS,verbose_name="Relationship")

#     def __str__(self):
#         return f'{self.relationship}'.format()


class Assesement(models.Model):
    TYPES = (
        ('bt', 'Begining Of Term'),
         ('mt', 'Mid Term'),
        ('et', 'End Of Term'),
    )
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Subject")
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name="Study Term")
    type = models.CharField(max_length=100,choices=TYPES, verbose_name="Assesement Type")
    date = models.DateField(auto_now_add=True)
    score = models.PositiveIntegerField(verbose_name="Marks Scored")

    def __str__(self):
        return self.score


    

    

    