from django.urls import path
from . import views

urlpatterns = [
    # 🔐 AUTENTICACIÓN
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('inicio/', views.index, name='index'), 

    # 📦 MÓDULOS PRINCIPALES
    path('productos/', views.productos, name='productos'),
    path('clientes/', views.clientes, name='clientes'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('vendedores/', views.vendedores, name='vendedores'),
    path('ventas/', views.ventas, name='ventas'),
    path('quien_soy/', views.quien_soy, name='quien_soy'),

    # 🧱 FORMULARIOS DE CREACIÓN
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('clientes/nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('sucursales/nueva/', views.nueva_sucursal, name='nueva_sucursal'),
    path('vendedores/nuevo/', views.nuevo_vendedor, name='nuevo_vendedor'),
    path('ventas/nueva/', views.nueva_venta, name='crear_venta'),

    # ✏️ ACCIONES - PRODUCTOS
    path('productos/editar/<int:id_producto>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),

    # ✏️ ACCIONES - CLIENTES
    path('clientes/editar/<int:id_cliente>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:id_cliente>/', views.eliminar_cliente, name='eliminar_cliente'),

    # ✏️ ACCIONES - SUCURSALES
    path('sucursales/editar/<int:id_sucursal>/', views.editar_sucursal, name='editar_sucursal'),
    path('sucursales/eliminar/<int:id_sucursal>/', views.eliminar_sucursal, name='eliminar_sucursal'),

    # ✏️ ACCIONES - VENDEDORES
    path('vendedores/editar/<int:id_vendedor>/', views.editar_vendedor, name='editar_vendedor'),
    path('vendedores/eliminar/<int:id_vendedor>/', views.eliminar_vendedor, name='eliminar_vendedor'),

    # ✏️ ACCIONES - VENTAS
    path('ventas/editar/<int:id_venta>/', views.editar_venta, name='editar_venta'),
    path('ventas/eliminar/<int:id_venta>/', views.eliminar_venta, name='eliminar_venta'),
]
