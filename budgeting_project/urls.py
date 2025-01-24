from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("", include("budgeting.urls")),
    path("admin/", admin.site.urls),
]