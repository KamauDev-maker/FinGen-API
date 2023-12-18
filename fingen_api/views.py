from rest_framework import status, generics
from .models import Quotation, Invoice, LedgerAccount, item, QuotationItem
from .serializers import QuotationSerializer, InvoiceSerializer, LedgerAccountSerializer, ItemSerializer, QuotationItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def create_quotation(request):
    serializer = QuotationSerializer(data=request.data)
    if serializer.is_valid():
        items_data = request.data.get('items', [])

        quotation = serializer.save()
        
        total_amount = sum(item_data['item']['price'] * item_data['quantity'] for item_data in items_data)
        
        for item_data in items_data:
            item_serializer = ItemSerializer(data=item_data['item'])
            if item_serializer.is_valid():
                item = item_serializer.save()
                QuotationItem.objects.create(quotation=quotation, item=item, quantity=item_data['quantity'])
        
        quotation.total_amount = total_amount
        quotation.save()       
        
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
        
        ledger_accounts = self.get_queryset()
        serializer = self.get_serializer(ledger_accounts, many=True)
        response_data = {
            'total_amount': total_amount,
            'ledger_accounts': serializer.data,
        }
        
        return Response(response_data, status=status.HTTP_200_OK)