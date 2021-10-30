from django.contrib import admin

from django_blank_and_null_fields.core.models import Exemplo


class ExemploAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'campo_1', 'campo_2', 'campo_3', 'campo_4')


admin.site.register(Exemplo, ExemploAdmin)
