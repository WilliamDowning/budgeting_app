from django import forms
from .models import Transaction

## Sets Form class to Transaction model and labels all fields requiring input
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["name", "category", "amount", "transaction_type"]