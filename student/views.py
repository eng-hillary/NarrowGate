from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import (
    ListView, 
    DetailView,
    View,
    DeleteView,
    UpdateView,
    TemplateView)
from django.views.generic.edit import CreateView

from . models import Student
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import StudentForm
from django.urls import reverse_lazy
from . filters import StudentFilter
from bootstrap_datepicker_plus.widgets import DatePickerInput

from payment.models import Payment
from payment.forms import PaymentForm

class StudentListView(LoginRequiredMixin, TemplateView):
    # model = Student
    # template_name = 'student/students_list.html'
    # context_object_name = 'students'

    def get(self, request):
        students = StudentFilter(request.GET, queryset=Student.objects.all())
        return render(request, 'student/students_list.html', {'students': students})


class StudentDetailView(LoginRequiredMixin,View):
    model = Payment
    # context_object_name = 'student'
    template_name = 'student/student_detail.html'

    def get(self, request, *args, **kwargs):

        context = {}
        form = PaymentForm()
        student = Student.objects.get(id=kwargs['pk'])
        payments = Payment.objects.filter(student=student)
        print("payments-->", payments)
        context['payment_form'] = form
        context['student'] = student
        context['payments'] = payments
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = PaymentForm(request.POST)
        student = Student.objects.get(id=kwargs['pk'])
        if form.is_valid():
            payment = form.save(commit=False)
            payment.student = student
            payment.save()
            return redirect(request.path_info)
        context['payment_form'] = form   
        return render(request, self.template_name, context)


class StudentCreateView(LoginRequiredMixin, CreateView):
    form_class = StudentForm
    template_name = 'student/student_create.html'
    success_url = reverse_lazy('student:students-list')

    def get_form(self):
        """
        retrieving the form object inorder to
        modify form fields 
        """
        form = super().get_form()
        form.fields['birth_date'].widget = DatePickerInput()
        return form

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student/student_delete.html'
    success_url = reverse_lazy('student:students-list')
    
    def get_object(self, **kwargs):
        obj = get_list_or_404(Student, id=self.kwargs['pk'])[0]
        return obj

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'student/student_update.html'
    form_class = StudentForm
    # success_url = reverse_lazy('student:students-list')


   
