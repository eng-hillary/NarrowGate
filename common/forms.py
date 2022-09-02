from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from . models import (
    Subject,
    Class, 
    Term
)

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['code', 'name', 'class_taught']

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['code'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Subject Code'})
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Subject Name'})
        self.fields['class_taught'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Class Taught'})

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Class Name'})
    
class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ['name', 'start_date', 'end_date']
        Widgets = {
             'start_date': DatePickerInput(),
              'end_date': DatePickerInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['code'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Subject Code'})
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Subject Name'})
        self.fields['class_taught'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Class Taught'})

