from django.db import models


class Banco(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.nombre)


class CuentaBancaria(models.Model):
    numero_de_cuenta = models.CharField(max_length=100)
    banco = models.ForeignKey(Banco)

    def __unicode__(self):
        return unicode(self.numero_de_cuenta + " - " + self.banco.nombre)
