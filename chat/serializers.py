from django rest_framework import serializers
from chat.models import Mensaje
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  contraseña = serializers.CharField(write_only= True)
  class Meta:
    model = User
    fields = ['username','password']

class MensajeSerializer(serializers.ModelSerializer):
  emisor = serializers.SlugRelatedField(
    many = False,
    slug_field = 'username',
    queryset = User.objects.all()
  )
  destinatario = serializers.SlugRelatedField(
    many = False,
    slug_field = 'username',
    queryset = User.objects.all()
  )
  class Meta:
    model = Mensaje
    fields = ['emisor', 'destinatario','mensaje','timestamp','tag']
    