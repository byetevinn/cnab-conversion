from django.urls import path
from .views import TransactionView

urlpatterns = [
    path("transactions/", TransactionView.as_view()),
]
