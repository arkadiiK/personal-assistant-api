from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from django.utils import timezone

from finance.models import Transaction
from events.models import Event
from events.serializers import EventSerializer


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # finances
        user_transactions = Transaction.objects.filter(user=self.request.user)
        income = user_transactions.filter(
            type=Transaction.TransactionType.INCOME
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        expense = user_transactions.filter(
            type=Transaction.TransactionType.EXPENSE
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        balance = income - expense

        # events
        next_event = Event.objects.filter(
            user=request.user,
            start_time__gt=timezone.now(),
        ).order_by('start_time').first()

        if next_event:
            next_event_data = EventSerializer(next_event).data
        else:
            next_event_data = None

        return Response({
            'username': request.user.username,
            'finance': {
                'balance': balance,
                'total_income': income,
                'total_expense': expense,
            },
            'next_event': next_event_data
        })
