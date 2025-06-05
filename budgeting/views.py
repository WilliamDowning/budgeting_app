from django.shortcuts import render, redirect, get_object_or_404
from .forms import TransactionForm
from .models import Transaction
from django.utils.timezone import now
from budgeting.firebase_config import save_transaction_to_firestore, update_transaction_in_firestore, delete_transaction_in_firestore, db
from django.http import JsonResponse

def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.created_at = now()
            transaction.save()
            save_transaction_to_firestore(transaction)  # Firestore will generate the ID
            return redirect("transaction_list")
    else:
        form = TransactionForm()
    return render(request, "budgeting/add_transaction.html", {"form": form})

def transactions_list(request):
    if request.method == "POST":
        transaction_id = request.POST.get("transaction_id")  # Get transaction_id from POST data
        if transaction_id:
            transaction = get_object_or_404(Transaction, id=transaction_id)
            try:
                delete_transaction_in_firestore(transaction)  # Attempt Firestore deletion first
                transaction.delete()  # Only delete from the database if Firestore deletion succeeds
                return JsonResponse({"success": True})
            except Exception as e:
                print(f"Error deleting transaction from Firestore: {e}")
                return JsonResponse({"success": False, "error": "Failed to delete from Firestore"}, status=500)
        return JsonResponse({"success": False}, status=400)

    transactions = db.collection("transactions").stream()
    transaction_data = [
        {
            "id": t.id,
            **t.to_dict(),
        }
        for t in transactions
    ]
    return render(request, "budgeting/transaction_list.html", {"transactions": transaction_data})

def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if (form.is_valid()) and (form.has_changed()):
                transaction = form.save(commit=False)
                transaction.save()
                update_transaction_in_firestore(transaction)
                return redirect("transaction_list")
        else:
            print("Form is not valid or has not changed.")
            return redirect("transaction_list")
    else:
        form = TransactionForm(instance=transaction)
    return render(request, "budgeting/edit_transaction.html", {"form": form, "transaction": transaction})

