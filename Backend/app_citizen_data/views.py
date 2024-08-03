from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

class SearchByName(APIView):
    def get(self, request, name):
        try:
            citizen = Citizen.objects.get(name__contains=name)
            serializer = CitizenSerializer(citizen)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Citizen.DoesNotExist:
            return Response({'error': 'Citizen not found'}, status=status.HTTP_404_NOT_FOUND)

class SearchByBankAc(APIView):
    def get(self, request, account):
        try:
            bank = BankAccount.objects.get(account_number=account)
            serializer = CitizenSerializer(bank.citizen)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Citizen.DoesNotExist:
            return Response({'error': 'Citizen not found'}, status=status.HTTP_404_NOT_FOUND)
        
class SearchByPhone(APIView):
    def get(self, request, number):
        try:
            phone = PhoneNumber.objects.get(number=number)
            serializer = CitizenSerializer(phone.citizen)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Citizen.DoesNotExist:
            return Response({'error': 'Citizen not found'}, status=status.HTTP_404_NOT_FOUND)
        
class SearchByCitizenship(APIView):
    def get(self, request, number):
        try:
            citizenship = Citizenship.objects.get(number=number)
            serializer = CitizenSerializer(citizenship.citizen)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Citizen.DoesNotExist:
            return Response({'error': 'Citizen not found'}, status=status.HTTP_404_NOT_FOUND)