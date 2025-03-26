from django.db import models
##Defines for the database to set default values of income and expense
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("income", "Income"),
        ("expense", "Expense"),
    ]
    ##Defines each variable type for Firestore
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2 )
    transaction_type = models.CharField(max_length=10, choices = TRANSACTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    ##Return function to return name, transaction_type and amount of current transaction
    def __str__(self):
        return f"{self.name} ({self.transaction_type}): ${self.amount}"

  


