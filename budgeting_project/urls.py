from django.urls import path, include
from django.contrib import admin
from graphene_django.views import GraphQLView
from budgeting.schema import schema

urlpatterns = [
    path("", include("budgeting.urls")),
    path("admin/", admin.site.urls),
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]