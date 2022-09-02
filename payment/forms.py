from turtle import width
from django import forms
from . models import (
    Fee, 
    Invoice, 
    Payment,
    Arear
    )

from bootstrap_modal_forms.forms import BSModalModelForm
from bootstrap_modal_forms.forms import BSModalModelForm

class FeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Class Name'})
        self.fields['amount'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Class Stream'})

    class Meta:
        model = Fee
        fields = ['name', 'amount']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('title','student', 'telephone')
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Title'})
        self.fields['student'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Student'})
        self.fields['telephone'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Telephone'})

# class PaymentModelForm(BSModalModelForm):
#     class Meta:
#         model = Payment
#         fields = ('fee','invoice', 'mode', 'term', 'amount')
        

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('fee', 'mode', 'amount')
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fee'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Fee'})
        self.fields['mode'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Mode'})
        self.fields['amount'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Amount'})
        
        
class SearchForm(forms.Form):
    student_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control form-control-dark w-50 bg-light',
            'placeholder': 'Student Number'
             }))