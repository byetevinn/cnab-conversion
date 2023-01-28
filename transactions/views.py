from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TransactionSerializer
from .models import Transaction


class TransactionView(ListCreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class TransactionDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
