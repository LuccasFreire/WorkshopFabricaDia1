from django.urls import path
from . import views
from django.conf.urls import include
from django.contrib import admin
from . import loja_api


urlpatterns = [
    path('', include(loja_api.views)),
    path('admin/', admin.site.urls),
    #path('Cliente/', views.ClienteLista.as_view(), name = 'lista_cliente'),
]
