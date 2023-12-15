from django.db import models

# Create your models here.
class Quotation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    
class Invoice(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    sent = models.BooleanField(default=False)
    
class LedgerAccount(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)