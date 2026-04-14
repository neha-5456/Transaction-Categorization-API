from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer
from services.categorization_service import CategorizationService

class CategorizeTransactionView(APIView):

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)

        if serializer.is_valid():
            service = CategorizationService()
            result = service.categorize(serializer.validated_data)
            return Response(result)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)