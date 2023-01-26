# Generated by Django 4.1.5 on 2023-01-26 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0003_alter_transaction_cpf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="date",
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="hour",
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="type",
            field=models.CharField(
                choices=[
                    (1, "Débito"),
                    (2, "Boleto"),
                    (3, "Financiamento"),
                    (4, "Crédito"),
                    (5, "Recebimento Empréstimo"),
                    (6, "Vendas"),
                    (7, "Recebimento TED"),
                    (8, "Recebimento DOC"),
                    (9, "Aluguel"),
                ],
                max_length=22,
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="value",
            field=models.CharField(max_length=10),
        ),
    ]