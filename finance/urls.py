from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TransactionsViewSet, TransactionStatsView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'transactions', TransactionsViewSet, basename='transactions')
urlpatterns = [
    path('', include(router.urls)),
    path('stats/', TransactionStatsView.as_view(), name='stats'),
]
