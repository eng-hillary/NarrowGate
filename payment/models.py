from typing_extensions import Required
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4

from student.models import Student, Term
from common.models import Class



class Fee(models.Model):
    name = models.CharField(max_length=100,verbose_name='Fee Name' )
    classes = models.ManyToManyField(Class)
    payment_deadline = models.DateTimeField(blank=True, null=True)
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, null=True,verbose_name='Study Term')
    amount = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
 
    
    class Meta:
        verbose_name_plural = 'Fees'

    def __str__(self):
        return self.name

class Invoice(models.Model):
    STATUSES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('expired', 'Expired')
    )

    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, null=True, blank=True, default='Payment Invoice')
    status = models.CharField(max_length=100, choices=STATUSES, default='pending', verbose_name='Payment Mode')
    grand_total = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
    telephone = models.CharField(max_length=100, null=True, blank=True)

    #Utility fields
    invoice_number = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.invoice_number, self.grand_total)


    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.invoice_number is None:
            self.invoice_number = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.invoice_number, self.date_created))

        self.slug = slugify('{} {}'.format(self.invoice_number, self.date_created))
        self.last_updated = timezone.localtime(timezone.now())

        super(Invoice, self).save(*args, **kwargs)


class Payment(models.Model):
    MODES = (
        ('cash', 'Cash Payment'),
        ('bank', 'Bank Payment'),
        ('mobile', 'Mobile Money')
    )

    fee = models.ForeignKey(Fee, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    mode = models.CharField(max_length=100, choices=MODES, default='cash', verbose_name='Payment Mode')
    date_paid = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)

    def __str__(self):
        return str(self.amount)

class Arear(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    fee = models.ForeignKey(Fee, on_delete=models.SET_NULL, null=True)
    initial_amount = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
    amount_paid = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
    pending_balance = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)

    def __str__(self):
        return '{}'.format(self.fee)




