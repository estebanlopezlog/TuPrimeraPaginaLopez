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
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import UserProfile


# 🌐 PÁGINAS PRINCIPALES
@login_required(login_url='login')
def index(request):
    return render(request, 'entidades/index.html')

##@login_required(login_url='login')
##@permission_required('aplicacion.view_producto', raise_exception=True)
##def productos(request):
##    productos = Producto.objects.all()
##    return render(request, 'entidades/productos.html', {'productos': productos})

@login_required(login_url='login')
@permission_required('aplicacion.view_producto', raise_exception=True)
def productos(request):
    query = request.GET.get('q', '')  # Captura el texto del filtro
    if query:
        productos = Producto.objects.filter(nombre_producto__icontains=query)
    else:
        productos = Producto.objects.all()

    return render(request, 'entidades/productos.html', {
        'productos': productos,
        'query': query
    })


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



# REGISTRO DE NUEVOS USUARIOS
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        profile_picture = request.FILES.get('profile_picture')

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'entidades/register.html')

        if len(password1) < 8 or password1.isdigit() or password1.lower() in ['password', 'contraseña', '12345678']:
            messages.error(request, "La contraseña no cumple los requisitos de seguridad.")
            return render(request, 'entidades/register.html')

        try:
            user = User.objects.create_user(
                username=username,
                password=password1,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user.save()

            # Crear el perfil y asociar la imagen
            profile = UserProfile(user=user)
            if profile_picture:
                profile.profile_picture = profile_picture
            profile.save()

            messages.success(request, "Usuario registrado exitosamente. Ahora podés iniciar sesión.")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "El nombre de usuario ya existe. Elegí otro.")
            return render(request, 'entidades/register.html')

    return render(request, 'entidades/register.html')


# Para editar el perfil de usuario
@login_required(login_url='login')
def editar_perfil(request):
    user = request.user
    perfil, creado = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        profile_picture = request.FILES.get('profile_picture')

        # Actualizar datos del usuario
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        # Actualizar imagen de perfil
        if profile_picture:
            perfil.profile_picture = profile_picture
        perfil.save()

        messages.success(request, "✅ Perfil actualizado correctamente.")
        return redirect('index')

    context = {'user': user, 'perfil': perfil}
    return render(request, 'entidades/editar_perfil.html', context)

## Vista adicional - DASHBOARD

from django.db.models import Sum, Count
from django.utils.dateparse import parse_date
from datetime import date
import pandas as pd

@login_required(login_url='login')
def dashboard(request):
    # Captura de filtros
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    # Definir rango por defecto (últimos 30 días)
    if not fecha_inicio or not fecha_fin:
        fecha_fin = date.today()
        fecha_inicio = fecha_fin.replace(day=1)

    # Convertir a tipo fecha
    fecha_inicio = parse_date(str(fecha_inicio))
    fecha_fin = parse_date(str(fecha_fin))

    # Filtrar ventas en el rango
    ventas = Venta.objects.filter(fecha_hora_venta__date__range=[fecha_inicio, fecha_fin])

    # 1️⃣ Clientes nuevos por día
    clientes_por_dia = (
        Cliente.objects.filter(fecha_alta__range=[fecha_inicio, fecha_fin])
        .values('fecha_alta')
        .annotate(total=Count('id_cliente'))
        .order_by('fecha_alta')
    )

    # 2️⃣ Total de ventas
    total_ventas = ventas.count()

    # 3️⃣ Total vendido (solo tarjetas)
    total_tarjeta = ventas.filter(forma_de_pago='TARJETA').aggregate(total=Sum('detalleventa__precio_total'))['total'] or 0

    # 4️⃣ Top vendedores
    top_vendedores = (
        ventas.values('vendedor__nombre_vendedor', 'vendedor__apellido_vendedor')
        .annotate(total=Sum('detalleventa__precio_total'))
        .order_by('-total')[:5]
    )

    # 5️⃣ Distribución por forma de pago
    ventas_por_pago = (
        ventas.values('forma_de_pago')
        .annotate(total=Sum('detalleventa__precio_total'))
    )

    context = {
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'clientes_por_dia': clientes_por_dia,
        'total_ventas': total_ventas,
        'total_tarjeta': total_tarjeta,
        'top_vendedores': top_vendedores,
        'ventas_por_pago': ventas_por_pago,
    }

    return render(request, 'entidades/dashboard.html', context)
