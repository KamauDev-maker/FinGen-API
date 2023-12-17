from django.urls import path
from .views import create_quotation, InvoiceListCreateView, LedgerAccountListCreateView

urlpatterns = [
    path('quotations/', create_quotation, name='quotation-list-create'),
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('ledger-accounts/', LedgerAccountListCreateView.as_view(), name='ledger-account-list-create'),
]