from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("add/", views.add_transaction, name="add_transaction"),
    path("edit/<str:transaction_id>/", views.edit_transaction, name="edit_transaction"),
    path("", views.transactions_list, name="transaction_list"),
]