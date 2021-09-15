from django.contrib import admin

from .models import Cliente, Avaliacao


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')
