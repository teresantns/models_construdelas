from django.db import models
from uuid import uuid4

# Create your models here.



class Conta(models.Model):
    numero = models.UUIDField(primary_key=True, default=uuid4, editable=False) # numero feio
    saldo = models.FloatField(default=100, blank=False)

    def __str__(self):
        details = f'Conta de número {self.numero}. Saldo atual: {self.saldo} '
        return details


class Cliente(models.Model):
    name = models.CharField(max_length=255, blank=False)
    cpf = models.CharField(max_length=11, blank=False, primary_key=True)
    email = models.EmailField(max_length=255, blank=False)
    creation = models.DateField(auto_now=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='conta')

    def __str__(self):
        # details = f'Cliente {self.name} de conta {self.conta}'
        return self.name

class Transferencia(models.Model):
    date = models.DateField(auto_now=True)
    origem = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, related_name='cliente_origem')
    destino = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, related_name='cliente_destino')
    valor = models.FloatField(default=0)

    def __str__(self):
        details = f'Trasferência do usuário de cpf {self.origem} para o usuário de cpf {self.destino} no valor de {self.valor} realizada em {self.date}'
        return details
