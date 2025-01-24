import graphene
from budgeting.firebase_config import db

class TransactionType(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    amount = graphene.Float()
    category = graphene.String()
    transaction_type = graphene.String()
    created_at = graphene.String()

class Query(graphene.ObjectType):
    all_transactions = graphene.List(TransactionType)

    def resolve_all_transactions(root, info):
        transactions = db.collection('transactions').stream()
        print("Firestore Documents:")
        for doc in transactions:
            print(doc.id, doc.to_dict())

        transactions = db.collection('transactions').stream()

        return [
            TransactionType(
                id=doc.id,
                name=doc.to_dict().get('name'),
                amount=doc.to_dict().get('amount'),
                category=doc.to_dict().get('category'),
                transaction_type=doc.to_dict().get('transaction_type'),
                created_at=doc.to_dict().get('created_at')
            )
            for doc in transactions
        ]

schema = graphene.Schema(query=Query)
