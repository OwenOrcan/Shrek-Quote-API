from django.http import JsonResponse
from .models import Quote
from .serializers import QuoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random


@api_view(['GET'])
def random_quote(request):
    count = Quote.objects.count()
    if count == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)
    random_index = random.randint(0, count - 1)
    item = Quote.objects.all()[random_index]
    serializer = QuoteSerializer(item)
    return Response(serializer.data)


@api_view(['POST'])
def add_quote(request):
    serializer = QuoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
