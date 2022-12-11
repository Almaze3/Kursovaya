from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mail
from .serializers import MailSerializer
import nickname
from django.shortcuts import render
from drf_spectacular.utils import extend_schema


# Create your views here.


class MailView(APIView):
    @extend_schema(request=MailSerializer, responses=MailSerializer)
    def get(self, request, mail):
        name = Mail(mail, nickname.nickname(mail))

        serializer_for_request = MailSerializer(instance=name)

        return Response(serializer_for_request.data)
