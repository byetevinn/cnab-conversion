from django.db import models


TRANSACTION_TYPE = {
    1: "Débito",
    2: "Boleto",
    3: "Financiamento",
    4: "Crédito",
    5: "Recebimento Empréstimo",
    6: "Vendas",
    7: "Recebimento TED",
    8: "Recebimento DOC",
    9: "Aluguel",
}


class Transaction(models.Model):
    type = models.CharField(choices=TRANSACTION_TYPE.items(), max_length=22)
    date = models.CharField(max_length=8)
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=6)
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
