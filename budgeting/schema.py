import graphene
from budgeting.firebase_config import db

class BudgetType(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    amount = graphene.Float()
    created_at = graphene.String()

class Query(graphene.ObjectType):
    all_budgets = graphene.List(BudgetType)

    def resolve_all_budgets(root, info):
        budgets = db.collection('budgets').stream()
        return [
            BudgetType(
                id=doc.id,
                name=doc.to_dict().get('name'),
                amount=doc.to_dict().get('amount'),
                created_at=doc.to_dict().get('created_at')
            )
            for doc in budgets
        ]

schema = graphene.Schema(query=Query)
