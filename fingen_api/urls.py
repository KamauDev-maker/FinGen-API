from django.urls import path
from .views import QuotationListCreateView, InvoiceListCreateView

urlpatterns = [
    path('quotations/', QuotationListCreateView.as_view(), name='quotation-list-create'),
    path('invoices/', InvoiceListCreateView.as_view(), name='nvoice-list-create'),
]