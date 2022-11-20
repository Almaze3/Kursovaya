from rest_framework import serializers


class MailSerializer(serializers.Serializer):
    mail = serializers.CharField()
    name = serializers.CharField()