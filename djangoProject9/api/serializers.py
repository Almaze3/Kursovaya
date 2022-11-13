from rest_framework import serializers


class MailSerializer(serializers.Serializer):
    mail = serializers.StringField()
    name = serializers.StringField()