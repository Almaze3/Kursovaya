from django.urls import path
from . import views


urlpatterns = [
    path('<str:mail>', views.index)
]