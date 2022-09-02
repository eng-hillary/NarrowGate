from django import forms
from . models import Student
from bootstrap_datepicker_plus.widgets import DatePickerInput

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_number','first_name', 'last_name','birth_date', 'circumstances', 'current_class', 
                    'current_term','address','phone','guardian_first','guardian_last','relationship',
                    'guardian_occupation','guardian_phone','guardian_email','guardian_address'
                    )
        widgets = {
            'birth_date': DatePickerInput()
            
        }

       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student_number'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Student Number'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Last Name'})
        self.fields['circumstances'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Special Circumstances'})
        self.fields['current_class'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Current Class'})
        self.fields['current_term'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Current Term'})
        self.fields['address'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Student Address'})
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Home Phone'})
        self.fields['guardian_first'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Guardian First Name'})
        self.fields['guardian_last'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Guardian Last Name'})
        self.fields['relationship'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Relationship'})
        self.fields['guardian_occupation'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Guardian Occupation'})
        self.fields['guardian_phone'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Guardian Telephone'})
        self.fields['guardian_email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Guardian Email'})
        self.fields['guardian_address'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Guardian Address'})

       