from django.urls import path
from .views import CategorizeTransactionView

urlpatterns = [
    path('categorize/', CategorizeTransactionView.as_view()),
]