from django.urls import path
from .views import QuotationListCreateView, InvoiceListCreateView, LedgerAccountListCreateView

urlpatterns = [
    path('quotations/', QuotationListCreateView.as_view(), name='quotation-list-create'),
    path('invoices/', InvoiceListCreateView.as_view(), name='nvoice-list-create'),
    path('ledger/', LedgerAccountListCreateView.as_view(), name='legder-account-created'),
]