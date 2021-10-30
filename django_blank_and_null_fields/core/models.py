from django.db import models


class Exemplo(models.Model):
    descricao = models.CharField("descrição", max_length=30)
    campo_1 = models.CharField(max_length=10)                           # blank=False,  null=False
    campo_2 = models.CharField(max_length=10, blank=True)               # blank=True,   null=False
    campo_3 = models.CharField(max_length=10, null=True)                # blank=False,  null=True
    campo_4 = models.CharField(max_length=10, blank=True, null=True)    # blank=False,  null=False

    def __str__(self):
        return self.descricao
