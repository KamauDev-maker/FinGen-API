from rest_framework import serializers
from .models import Quotation, Invoice, LedgerAccount, Item, QuotationItem

class ItemSerializer(serializers.ModelSerial):
    class Meta:
        model = Item
        fields = '__all__'
        
class QuotationItemSerializer(serializers.ModelSerial):
    item = ItemSerializer()
    
    class Meta:
        model = QuotationItem
        fields = ['item', 'quantity']

class QuotationSerializer(serializers.ModelSerializer):
    items = QuotationItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Quotation
        fields = '__all__'
        extra_kwargs = {'expiration_date': {'required': False}}
        
class InvoiceSerializer(serializers.ModelSerializer):
    quotation = QuotationSerilier()
    
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