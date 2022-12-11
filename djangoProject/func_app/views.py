from django.shortcuts import render
from django import forms
from django.http import HttpResponse

import nickname


# Create your views here.
class UserForm(forms.Form):
    SendMeText = forms.CharField()


def index(request):
    if request.method == 'POST':
        mail = request.POST.get('SendMeText')
        origin = mail
        return HttpResponse(f"<h1>Имя пользователя {origin}: {nickname.nickname(mail)}<h1>")
    else:
        useform = UserForm()
        return render(request, 'index.html', {'form': useform})
