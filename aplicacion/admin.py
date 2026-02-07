from django.contrib import admin
from .models import Cliente, Producto, Venta

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'apellido_cliente', 'localidad', 'codigo_postal')
    search_fields = ('nombre_cliente', 'apellido_cliente', 'dni')
    list_filter = ('localidad',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'precio_unitario', 'proveedor')
    list_filter = ('proveedor',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'vendedor', 'sucursal', 'fecha_hora_venta', 'forma_de_pago')
    list_filter = ('forma_de_pago', 'sucursal')
    date_hierarchy = 'fecha_hora_venta'

admin.site.site_header = "Panel de Control Logístico - TuPrimeraPaginaLopez"
admin.site.site_title = "Gestión Logística Comercial"
admin.site.index_title = "Administración General del Sistema"
