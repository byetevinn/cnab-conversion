from rest_framework.generics import CreateAPIView
from .serializers import TransactionSerializer
from .models import Transaction


class TransactionView(CreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def create(self, request, *args, **kwargs):

        print(request.data)

        return super().create(request, *args, **kwargs)
