from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
  emisor= models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'emisor')
  destinatario = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'destinatario')
  mensaje  = models.CharField(max_length = 1000)
  tag = models.CharField(max_length = 100)
  timestamp = models.DateTimeField(auto_now_add = True)
  def __str__(self):
    return self.mensaje
  class Meta:
    ordering = ('timestamp',)

# Create your models here.
