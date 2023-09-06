from django.contrib import admin
from guia.models import Servicio, Estado, Liquidador, GuiaDespacho, GuiaEstado, DespachoCiudad, GuiaCliente, GuiaServicio

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Estado)
admin.site.register(Liquidador)
admin.site.register(GuiaDespacho)
admin.site.register(GuiaEstado)
admin.site.register(DespachoCiudad)
admin.site.register(GuiaCliente)
admin.site.register(GuiaServicio)
