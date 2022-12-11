from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from djangoProject9 import views
from func_app import views
from api import views
from . import settings
from func_app.views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="functional"),
    path('func_app/', include('func_app.urls')),
    path('api/<str:mail>', views.MailView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",
    ),
]
