from django.db import models
from datetime import timedelta

# Create your models here.
class Quotation(models.Model):
    customer_name = models.CharField(max_length=255)
    items = models.JSONField()
    number_of_items = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    issue_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    is_accepted = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        # Automatically set the expiration
        if not self.expiration_date:
            self.expiration_date = self.issue_date + timedelta(days=7)
            
        self.total_amount = self.price * self.number_of_items
        super().save(*args, **kwargs)
    
class Invoice(models.Model):
    quotation = models.OneToOneField(Quotation, on_delete=modles.CASCADE)
    invoice_number =models.CharField(max_length=20, unique=True)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = f'INV-{self.quotation.id}'
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