from django.http import HttpResponse
import nickname


# Create your views here.

def index(request, mail):
    return HttpResponse(f"Имя пользователя {mail}: {nickname.nickname(mail)}")
