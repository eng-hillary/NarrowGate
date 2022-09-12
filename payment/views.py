from ast import For
from email.feedparser import FeedParser
from multiprocessing import get_context
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    View,
    DetailView,
    FormView
    )
from django.views.generic.edit import UpdateView
from bootstrap_modal_forms.generic import BSModalCreateView
from student.models import Student
from . models import Invoice, Payment, Arear
from . forms import (
    InvoiceForm,
    FeeForm,
    PaymentForm,
    SearchForm
     )


class PaymentsView(LoginRequiredMixin, TemplateView):
    template_name = 'payment/payments.html'
    def get(self, request, *args, **kwargs):
        payments = Payment.objects.all()
        return render(request, self.template_name, {'payments':payments})

class PayementSearchView(LoginRequiredMixin, FormView):
    # form_class =  SearchForm
    template_name = 'payment/search.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm()

        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)  
        if form.is_valid():
            student_number = form.cleaned_data['student_number']
            try:
                student=Student.objects.get(student_number=student_number)
               
                # return render(request, 'payment/make_payment.html', {'student':student})
                return redirect('payment:payment-create')
            except:
                return render(request, self.template_name, {
                    'form': form,
                    'error': 'No student with that student number'}
                    )            

    def form_valid(self, form):
        return super().form_valid(form)


class PaymentCreateView(LoginRequiredMixin,CreateView):
    model = Payment
    form_class =  PaymentForm
    template_name = 'payment/payment_create.html'
 

    def get(self, request, *args, **kwargs):
        student = Student.objects.get(student_number=kwargs['student_number'])
        # student_arears = Arear.objects.filter(student=student)   
        form = self.form_class()
        # form.fields["fee"].queryset = student_arears
        # print("arears list", student_arears)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(student_number=kwargs['student_number'])
        form = self.form_class(request.POST)
        

        if form.is_valid():
            #getting the type of the fee being paid
            fee = form.cleaned_data['fee']
            amount= form.cleaned_data['amount']
            student = Student.objects.get(student_number=kwargs['student_number'])

            try:
                #getting student's arears being paid for
                arear = Arear.objects.get(student=student, fee=fee)
                #update the pending balance
                current_balance = arear.pending_balance
                new_balance = current_balance - amount 
                form.save()
                arear.pending_balance = new_balance 
                arear.save()
                return redirect('student:student-detail', pk=student.pk)

            except:
                return render(request, self.template_name, {'form':form, 'error': 'this studend does not have such areas'})

            

    def form_valid(self, form):
        return super().form_valid(form)


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = 'payment/invoices_list.html'
    context_object_name = 'invoices'

class CreateInvoiceView(LoginRequiredMixin, View):
    def get(self, request):
        invoice = Invoice.objects.create()
        return redirect('payment:invoice-update', slug=invoice.slug)

class InvoiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'payment/invoice_update.html'
    # fields = ['title', 'student', 'telephone']
    success_url = reverse_lazy('payment:invoice-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payments = Payment.objects.all()
        context['payments'] = payments
        return context

class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'payment/invoice_u'


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = 'payment/invoice-detail.html'
    context_object_name = 'invoice'



