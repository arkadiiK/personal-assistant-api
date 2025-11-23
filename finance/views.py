from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['category', 'type', 'date']
    search_fields = ['description', 'category__name']
    ordering_fields = ['date', 'amount']


class TransactionStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_transactions = Transaction.objects.filter(user=request.user)

        total_income_data = user_transactions.filter(
            type=Transaction.TransactionType.INCOME
        ).aggregate(Sum('amount'))

        total_expense_data = user_transactions.filter(
            type=Transaction.TransactionType.EXPENSE
        ).aggregate(Sum('amount'))

        total_income = total_income_data['amount__sum'] or 0
        total_expense = total_expense_data['amount__sum'] or 0
        balance = total_income - total_expense

        return Response({
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance
        })
