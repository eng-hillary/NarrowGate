from django.urls import URLPattern, path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.PaymentsView.as_view(), name='payments'),
    path('search/', views.PayementSearchView.as_view(), name='search-student'),
    path('create/<student_number>', views.PaymentCreateView.as_view(), name='payment-create'),
    path('update/<slug:slug>/', views.InvoiceUpdateView.as_view(), name='invoice-update'),
    path('detail/<slug:slug>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    # path('invoices/', views.InvoiceListView.as_view(), name='invoice-list'),
    # path('invoice/<slug:slug>/', views.PaymentCreateView.as_view(), name='payment-create'),
    # path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student-delete'),
] 