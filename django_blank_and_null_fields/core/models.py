from django.db import models


class Exemplo(models.Model):
    descricao = models.CharField("descrição", max_length=30)
    campo_1 = models.IntegerField(default=10)             # blank=False,  null=False
    campo_2 = models.IntegerField(blank=True, null=True)  # blank=True,   null=True
    campo_3 = models.IntegerField(null=True)              # blank=False,  null=True
    campo_4 = models.IntegerField(blank=True)             # blank=True,   null=False

    def __str__(self):
        return self.descricao
