from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parses import JSONParser
from chat.models import Mensaje
from chat.serializers import MensajeSerializer,UserSerializer

@csrf_exempt

def lista_usuarios(request,pk = None):

  if request.method == 'GET':
    if pk:
      users = User.objects.filter(id = pk)
    else:
      users = User.objects.all()

    serializer = UserSerializer(users, many = True,context = {'request':request})
    return JsonResponse(serializer.data, safe = False)
  
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = UserSerializer(data = data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status = 201)
    return JsonResponse(serializer.errors, status = 400)

@csrf_exempt

def lista_mensajes(request, emisor = None,destinatario = None):
  if request.method == 'GET':
    mensajes = Mensaje.objects.filter(id_emisor = emisor, id_destinatario = destinatario)
    serializer = MensajeSerializer(mensaje, many = True, context={'request':request})
    return JsonResponse(serializer.data, safe = False)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = MensajeSerializer(data = data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status = 201)
    return JsonResponse(serializer.errors, status = 400)
# Create your views here.
