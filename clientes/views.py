from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cliente, Avaliacao
from .serializers import ClienteSerializer, AvaliacaoSerializer


class ClienteAPIView(APIView):
    """
    API de Clientes
    """
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)


class AvaliacaoAPIView(APIView):
    """
    API Avaliacoes
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)