# Generated by Django 4.1.5 on 2023-01-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0002_alter_transaction_cpf_alter_transaction_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="cpf",
            field=models.CharField(max_length=11),
        ),
    ]
