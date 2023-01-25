from rest_framework import serializers
from .models import Transaction


class TrnsactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
