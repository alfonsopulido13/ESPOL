from django.contrib import admin

# Register your models here.

from aplicacion.models import producto, carrito, venta, usuario, tarjeta, codigo

admin.site.register(producto)
admin.site.register(carrito)
admin.site.register(venta)
admin.site.register(tarjeta)
admin.site.register(usuario)
admin.site.register(codigo)