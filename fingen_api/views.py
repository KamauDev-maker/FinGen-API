from rest_framework import generics
from .models import Quotation, Invoice, LedgerAccount
from .serializers import QuotationSerializer, InvoiceSerializer, LedgerAccountSerializer


class QuotationListCreateView(generics.ListCreateAPIView):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer
    
    def perform_create(self, serializer):
        quantity = self.request.data.get('quantity', 1)
        serializer.save(quantity=quantity)
        
class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
class LedgerAccountListCreateView(generics.ListCreateAPIView):
    queryset = LedgerAccount.objects.all()
    serializer_class = LedgerAccountSerializer