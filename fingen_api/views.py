from rest_framework import status, generics
from .models import Quotation, Invoice, LedgerAccount
from .serializers import QuotationSerializer, InvoiceSerializer, LedgerAccountSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def create_quotation(request):
    serializer = QuotationSerializer(data=request.data)
    if serializer.is_valid():
        price = serializer.validated_data.get('price', 0.0)
        number_of_items = serializer.validated_data.get('number_of_items')
        total_amount = price * number_of_items

        
        quotation = serializer.save(total_amount=total_amount)
        
        invoice = Invoice(quotation=quotation, total_amount=total_amount)
        invoice.save()
        
        ledger, created = LedgerAccount.objects.get_or_create(customer_name=quotation.customer_name)
        ledger.update_balance(float(total_amount))
        
        
        invoice_serializer = InvoiceSerializer(invoice)
        return Response(invoice_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class LedgerAccountListCreateView(generics.ListCreateAPIView):
    queryset = LedgerAccount.objects.all()
    serializer_class = LedgerAccountSerializer
    
    def list(self, request, *args, **kwargs):
        total_amount = LedgerAccount.calculate_total_amount()
        return Response({'total_amount': total_amount, 'amount': total_amount}, status=status.HTTP_200_OK)