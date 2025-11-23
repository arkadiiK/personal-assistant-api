from rest_framework import serializers

from finance.models import Category, Transaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'user', 'name')
        read_only_fields = ('user',)


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'id',
            'type',
            'user',
            'amount',
            'category',
            'date',
            'description',
            'created_at',
            'user'
        )
        read_only_fields = ('user', 'created_at')
