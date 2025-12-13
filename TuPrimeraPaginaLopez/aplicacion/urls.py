from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('clientes/', views.clientes, name='clientes'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('vendedores/', views.vendedores, name='vendedores'),
    path('ventas/', views.ventas, name='ventas'),
    path('quien_soy/', views.quien_soy, name='quien_soy'),

    # Formularios
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('clientes/nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('sucursales/nueva/', views.nueva_sucursal, name='nueva_sucursal'),
    path('vendedores/nuevo/', views.nuevo_vendedor, name='nuevo_vendedor'),
    path('ventas/nueva/', views.nueva_venta, name='crear_venta'),
]
