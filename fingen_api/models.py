from django.db import models
from datetime import datetime, timedelta


# Create your models here.
class Quotation(models.Model):
    customer_name = models.CharField(max_length=255)
    items = models.ManyToManyField('Item', through='QuotationItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    issue_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(default=None, null=True)
    is_accepted = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.issue_date:
            self.issue_date = datetime.now().date()
        if not self.expiration_date:
            self.expiration_date = self.issue_date + timedelta(days=7)

        super().save(*args, **kwargs)
        self.calculate_total_amount()
        
    def calculate_total_amount(self):
        total_amount = sum(item.price * item.quantity for item in self.items.all())
        self.total_amount = total_amount
        self.save()
        
class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class QuotationItem(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
        
class Invoice(models.Model):
    quotation = models.OneToOneField(Quotation, on_delete=models.CASCADE)
    invoice_number =models.CharField(max_length=20, unique=True)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = f'INV-{self.quotation.id}'
        if not self.issue_date:
            self.issue_date = datetime.now().date()
        if not self.due_date:
            self.due_date = self.issue_date + timedelta(days=30)
        super().save(*args, **kwargs)
      
class LedgerAccount(models.Model):
    customer_name = models.CharField(max_length=255, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    last_updated = models.DateTimeField(auto_now_add=True)
    
    def update_balance(self, amount):
        self.balance += amount
        self.save()
        
    @classmethod
    def calculate_total_amount(cls):
        total_amount = cls.objects.aggregate(models.Sum('balance'))['balance__sum']
        return total_amount if total_amount is not None else 0.0