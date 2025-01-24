import firebase_admin
from firebase_admin import credentials, firestore
import os

# Define the path to your Firebase key file
key_path = os.path.join(
    os.path.dirname(__file__),  # Get the directory of the current file
    "../user_credentials/firebase_key.json"  # Relative path to the key
)

# Initialize Firebase app if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(key_path)
    firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()


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