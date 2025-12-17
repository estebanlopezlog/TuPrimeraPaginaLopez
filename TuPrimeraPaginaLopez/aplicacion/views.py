from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Producto, Cliente, Sucursal, Vendedor, Venta, DetalleVenta
from .forms import (
    ProductoForm, ClienteForm, SucursalForm, VendedorForm,
    VentaForm, DetalleVentaForm
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages



# 🌐 PÁGINAS PRINCIPALES
@login_required(login_url='login')
def index(request):
    return render(request, 'entidades/index.html')

@login_required(login_url='login')
@permission_required('aplicacion.view_producto', raise_exception=True)
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'entidades/productos.html', {'productos': productos})


@login_required(login_url='login')
@permission_required('aplicacion.view_cliente', raise_exception=True)
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'entidades/clientes.html', {'clientes': clientes})


@login_required(login_url='login')
@permission_required('aplicacion.view_sucursal', raise_exception=True)
def sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'entidades/sucursales.html', {'sucursales': sucursales})


@login_required(login_url='login')
@permission_required('aplicacion.view_vendedor', raise_exception=True)
def vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'entidades/vendedores.html', {'vendedores': vendedores})


@login_required(login_url='login')
@permission_required('aplicacion.view_venta', raise_exception=True)
def ventas(request):
    ventas = Venta.objects.all()
    datos_ventas = []
    for v in ventas:
        detalles = v.detalleventa_set.all()
        cantidad_total = sum([d.cantidad_vendida for d in detalles])
        total_venta = sum([d.precio_total for d in detalles])
        datos_ventas.append({
            'venta': v,
            'cantidad_total': cantidad_total,
            'total_venta': total_venta
        })
    return render(request, 'entidades/ventas.html', {'datos_ventas': datos_ventas})


def quien_soy(request):
    return render(request, 'entidades/quien_soy.html')


# --- PRODUCTOS ---
@login_required(login_url='login')
@permission_required('aplicacion.add_producto', raise_exception=True)
def nuevo_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('productos')
    return render(request, 'entidades/form_producto.html', {'form': form, 'titulo': 'Nuevo Producto'})


@login_required(login_url='login')
@permission_required('aplicacion.change_producto', raise_exception=True)
def editar_producto(request, id_producto):
    producto = Producto.objects.get(pk=id_producto)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect('productos')
    return render(request, 'entidades/form_producto.html', {'form': form, 'titulo': f'Editar Producto #{producto.id_producto}'})


@login_required(login_url='login')
@permission_required('aplicacion.delete_producto', raise_exception=True)
def eliminar_producto(request, id_producto):
    producto = Producto.objects.get(pk=id_producto)
    producto.delete()
    return redirect('productos')


# --- CLIENTES ---
@login_required(login_url='login')
@permission_required('aplicacion.add_cliente', raise_exception=True)
def nuevo_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes')
    return render(request, 'entidades/form_cliente.html', {'form': form, 'titulo': 'Nuevo Cliente'})


@login_required(login_url='login')
@permission_required('aplicacion.change_cliente', raise_exception=True)
def editar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('clientes')
    return render(request, 'entidades/form_cliente.html', {'form': form, 'titulo': f'Editar Cliente #{cliente.id_cliente}'})


@login_required(login_url='login')
@permission_required('aplicacion.delete_cliente', raise_exception=True)
def eliminar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    cliente.delete()
    return redirect('clientes')


# --- SUCURSALES ---
@login_required(login_url='login')
@permission_required('aplicacion.add_sucursal', raise_exception=True)
def nueva_sucursal(request):
    form = SucursalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sucursales')
    return render(request, 'entidades/form_sucursal.html', {'form': form, 'titulo': 'Nueva Sucursal'})


@login_required(login_url='login')
@permission_required('aplicacion.change_sucursal', raise_exception=True)
def editar_sucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(pk=id_sucursal)
    form = SucursalForm(request.POST or None, instance=sucursal)
    if form.is_valid():
        form.save()
        return redirect('sucursales')
    return render(request, 'entidades/form_sucursal.html', {'form': form, 'titulo': f'Editar Sucursal #{sucursal.id_sucursal}'})


@login_required(login_url='login')
@permission_required('aplicacion.delete_sucursal', raise_exception=True)
def eliminar_sucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(pk=id_sucursal)
    sucursal.delete()
    return redirect('sucursales')


# --- VENDEDORES ---
@login_required(login_url='login')
@permission_required('aplicacion.add_vendedor', raise_exception=True)
def nuevo_vendedor(request):
    form = VendedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vendedores')
    return render(request, 'entidades/form_vendedor.html', {'form': form, 'titulo': 'Nuevo Vendedor'})


@login_required(login_url='login')
@permission_required('aplicacion.change_vendedor', raise_exception=True)
def editar_vendedor(request, id_vendedor):
    vendedor = Vendedor.objects.get(pk=id_vendedor)
    form = VendedorForm(request.POST or None, instance=vendedor)
    if form.is_valid():
        form.save()
        return redirect('vendedores')
    return render(request, 'entidades/form_vendedor.html', {'form': form, 'titulo': f'Editar Vendedor #{vendedor.id_vendedor}'})


@login_required(login_url='login')
@permission_required('aplicacion.delete_vendedor', raise_exception=True)
def eliminar_vendedor(request, id_vendedor):
    vendedor = Vendedor.objects.get(pk=id_vendedor)
    vendedor.delete()
    return redirect('vendedores')


# --- VENTAS ---
DetalleVentaFormSet = modelformset_factory(DetalleVenta, form=DetalleVentaForm, extra=5)

@login_required(login_url='login')
@permission_required('aplicacion.add_venta', raise_exception=True)
def nueva_venta(request):
    form = VentaForm(request.POST or None)
    formset = DetalleVentaFormSet(request.POST or None, queryset=DetalleVenta.objects.none())

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            venta = form.save()
            for detalle_form in formset:
                if detalle_form.cleaned_data:
                    detalle = detalle_form.save(commit=False)
                    detalle.venta = venta
                    detalle.precio_total = detalle.cantidad_vendida * detalle.producto.precio_unitario
                    detalle.save()
            return redirect('ventas')
    return render(request, 'entidades/form_venta.html', {'form': form, 'formset': formset, 'titulo': 'Registrar Nueva Venta'})


@login_required(login_url='login')
@permission_required('aplicacion.change_venta', raise_exception=True)
def editar_venta(request, id_venta):
    venta = Venta.objects.get(pk=id_venta)
    form = VentaForm(request.POST or None, instance=venta)
    if form.is_valid():
        form.save()
        return redirect('ventas')
    return render(request, 'entidades/form_venta.html', {'form': form, 'titulo': f'Editar Venta #{venta.id_venta}'})


@login_required(login_url='login')
@permission_required('aplicacion.delete_venta', raise_exception=True)
def eliminar_venta(request, id_venta):
    venta = Venta.objects.get(pk=id_venta)
    venta.delete()
    return redirect('ventas')



# 🔐 LOGIN / LOGOUT
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'entidades/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



# 🚫 ERROR 403 

def error_403_view(request, exception=None):
    return render(request, 'entidades/403.html', status=403)

