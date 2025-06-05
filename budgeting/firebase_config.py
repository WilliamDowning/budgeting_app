import firebase_admin
from firebase_admin import credentials, firestore
import os
from decouple import config

##Grabs the path of firebase key, stores the credentials and creates the database connection
key_path = config("FIREBASE_KEY_PATH")
cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)
db = firestore.client()


## Saves any transaction based on data object variables, then sends transaction to firestore
def save_transaction_to_firestore(transaction):
    """Save a transaction to Firestore"""

    data = {
        "name": transaction.name,
        "category": transaction.category,
        "amount": float(transaction.amount),
        "transaction_type": transaction.transaction_type,
        "created_at": transaction.created_at.isoformat(),
    }
    doc_ref = db.collection("transactions").document()  # Let Firestore generate the ID
    doc_ref.set(data)
    transaction.id = doc_ref.id  # Save the Firestore-generated ID back to the transaction
    transaction.save()

def update_transaction_in_firestore(transaction):
    """Update a transaction in Firestore"""
    data = {
        "name" : transaction.name,
        "category" : transaction.category,
        "amount" : float(transaction.amount),
        "transaction_type" : transaction.transaction_type,
        "created_at" : transaction.created_at.isoformat(),
    }

    doc_ref = db.collection("transactions").document(transaction.id)
    doc_ref.update(data)

def delete_transaction_in_firestore(transaction):
    """Delete a transaction in Firestore"""
    try:
        doc_ref = db.collection("transactions").document(transaction.id)  # Use transaction.id directly
        doc_ref.delete()
        print(f"Transaction {transaction.id} deleted from Firestore.")
    except Exception as e:
        print(f"Error deleting transaction {transaction.id} from Firestore: {e}")
