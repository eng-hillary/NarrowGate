from ast import For
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
from . models import Invoice, Payment
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
    form_class =  SearchForm
    template_name = 'payment/search.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            student_number = form.cleaned_data['student_number']
            student = Student.objects.get(student_number=student_number)
            return render(request, 'payment/make_payment.html', {'student':student})
        return render(request, self.template_name, {'form': self.form_class})

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


class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'student/student_detail.html'

    def get(self, request, *args, **kwargs):

        form = self.form_class()
        context = {}
        context['payment_form'] = form
        context['data'] = "some data passed in from the view"
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {}
        context['payment_form'] = form   
        return render(request, self.template_name, context)


# class PaymentCreateView(BSModalCreateView):
#     template_name = 'payment/create_payment.html'
#     form_class = PaymentModelForm
#     success_message = 'Success: Payment was created.'
#     success_url = reverse_lazy('payment:invoice-detail')


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = 'payment/invoice-detail.html'
    context_object_name = 'invoice'



