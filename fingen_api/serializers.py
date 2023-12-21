from rest_framework import serializers
from .models import Quotation, Invoice, LedgerAccount

class QuotationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quotation
        fields = '__all__'
        extra_kwargs = {'expiration_date': {'required': False}}
   
class InvoiceSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source='quotation.customer_name')
    number_of_items = serializers.ReadOnlyField(source='quotation.number_of_items')
    price = serializers.ReadOnlyField(source='quotation.price')


    
    class Meta:
        model = Invoice
        fields = '__all__'
        
class LedgerAccountSerializer(serializers.ModelSerializer):
    number_of_items = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    
    class Meta:
        model = LedgerAccount
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
    
    def get_number_of_items(self, instance):
        last_quotation = Quotation.objects.filter(customer_name=instance.customer_name).last()
        return last_quotation.number_of_items if last_quotation else None
    
    def get_price(self, instance):
        last_quotation = Quotation.objects.filter(customer_name=instance.customer_name).last()
        return last_quotation.price if last_quotation else None