from django.db import models


# Create your models here.
class Mail:
    def __init__(self, mail, name):
        self.mail = mail
        self.name = name
