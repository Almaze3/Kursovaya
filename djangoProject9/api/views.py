from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mail
from .serializers import MailSerializer
import nickname
from django.shortcuts import render

# Create your views here.


class MailView(APIView):

    def get(self, request, mail):
        name = Mail(mail, nickname.nickname(mail))

        serializer_for_request = MailSerializer(instance=name)

        return Response(serializer_for_request.data)