from rest_framework import serializers
from .models import Quotation, Invoice, LedgerAccount

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = '__all__'
        extra_kwargs = {'expiration_date': {'required': False}}
        
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        
class LedgerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerAccount
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation