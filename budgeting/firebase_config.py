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
        "name" : transaction.name,
        "category" : transaction.category,
        "amount" : float(transaction.amount),
        "transaction_type" : transaction.transaction_type,
        "created_at" : transaction.created_at.isoformat(),
    }
    doc_ref = db.collection("transactions").document(transaction.id)
    doc_ref.set(data)