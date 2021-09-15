from django.urls import path

from .views import ClienteAPIView, AvaliacaoAPIView

urlpatterns = [
    path('clientes/', ClienteAPIView.as_view(), name='clientes'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
]