from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transaction
from django.utils.timezone import now
from budgeting.firebase_config import save_transaction_to_firestore, db

def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.created_at = now()
            transaction.id = transaction.created_at.strftime("%Y%m%d%H%M%S%f")
            transaction.save()
            save_transaction_to_firestore(transaction)
            return redirect("transaction_list")
    else:
        form = TransactionForm()
    return render(request, "budgeting/add_transaction.html", {"form": form})

def transactions_list(request):
    transactions = db.collection("transactions").stream()
    transaction_data = [
        {
            "id" : t.id,
            **t.to_dict(),
        }
        for t in transactions
    ]
    return render(request, "budgeting/transaction_list.html", {"transactions": transaction_data})