from django.urls import path
from . import views

urlpatterns = [
  path('api/mensajes/<int:emisor>/<int: destinatario>', views.lista_mensajes, name = 'detalle-mensajes'),
  path('api/mensajes/', views.lista_mensajes, name = 'lista-mensajes'),
  path('api/users/<int: pk>', views.lista_usuarios, name = 'detalle-usuarios')
  path('api/users/',views.lista_usuarios, name = 'lista-usuarios'),
]