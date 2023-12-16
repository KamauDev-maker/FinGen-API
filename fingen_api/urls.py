from django.urls import path
from .views import QuotationListCreateView, InvoiceListCreateView, LegderAccountListCreateView

urlpatterns = [
    path('quotations/', QuotationListCreateView.as_view(), name='quotation-list-create'),
    path('invoices/', InvoiceListCreateView.as_view(), name='nvoice-list-create'),
    path('ledger/', LegderAccountListCreateView.as_view(), name='legder-account-created'),
]