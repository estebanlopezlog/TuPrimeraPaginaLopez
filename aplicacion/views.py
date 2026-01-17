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
from django.db.models import Sum, Count
from django.utils.dateparse import parse_date
from datetime import date


# 🌐 PÁGINAS PRINCIPALES
@login_required(login_url='login')
def index(request):
    return render(request, 'entidades/index.html')


@login_required(login_url='login')
@permission_required('aplicacion.view_producto', raise_exception=True)
def productos(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre_producto__icontains=query) if query else Producto.objects.all()
    return render(request, 'entidades/productos.html', {'productos': productos, 'query': query})


@login_required(login_url='login')
@permission_required('aplicacion.view_cliente', raise_exception=True)
def clientes(request):
    return render(request, 'entidades/clientes.html', {'clientes': Cliente.objects.all()})


@login_required(login_url='login')
@permission_required('aplicacion.view_sucursal', raise_exception=True)
def sucursales(request):
    return render(request, 'entidades/sucursales.html', {'sucursales': Sucursal.objects.all()})


@login_required(login_url='login')
@permission_required('aplicacion.view_vendedor', raise_exception=True)
def vendedores(request):
    return render(request, 'entidades/vendedores.html', {'vendedores': Vendedor.objects.all()})


@login_required(login_url='login')
@permission_required('aplicacion.view_venta', raise_exception=True)
def ventas(request):
    ventas = Venta.objects.all()
    datos_ventas = []

    for v in ventas:
        detalles = v.detalleventa_set.all()
        datos_ventas.append({
            'venta': v,
            'cantidad_total': sum(d.cantidad_vendida for d in detalles),
            'total_venta': sum(d.precio_total for d in detalles),
        })

    return render(request, 'entidades/ventas.html', {'datos_ventas': datos_ventas})


def quien_soy(request):
    return render(request, 'entidades/quien_soy.html')


# --- CRUD PRODUCTOS ---
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
    Producto.objects.get(pk=id_producto).delete()
    return redirect('productos')


# 🔐 LOGIN / LOGOUT
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('index')
        messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'entidades/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# 🚫 ERROR 403
def error_403_view(request, exception=None):
    return render(request, 'entidades/403.html', status=403)


# 📝 REGISTRO (CORREGIDO – NO 500)
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        profile_picture = request.FILES.get('profile_picture')

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'entidades/register.html')

        if len(password1) < 8 or password1.isdigit():
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

            try:
                profile = UserProfile.objects.create(user=user)
                if profile_picture:
                    profile.profile_picture = profile_picture
                    profile.save()
            except Exception:
                user.delete()
                messages.error(request, "Error al crear el perfil de usuario.")
                return render(request, 'entidades/register.html')

            messages.success(request, "Usuario registrado correctamente.")
            return redirect('login')

        except IntegrityError:
            messages.error(request, "El nombre de usuario ya existe.")

    return render(request, 'entidades/register.html')


# 👤 EDITAR PERFIL
@login_required(login_url='login')
def editar_perfil(request):
    perfil, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        request.user.username = request.POST.get('username')
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.save()

        if request.FILES.get('profile_picture'):
            perfil.profile_picture = request.FILES.get('profile_picture')
            perfil.save()

        messages.success(request, "Perfil actualizado correctamente.")
        return redirect('index')

    return render(request, 'entidades/editar_perfil.html', {'perfil': perfil})


# 📊 DASHBOARD
@login_required(login_url='login')
def dashboard(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if not fecha_inicio or not fecha_fin:
        fecha_fin = date.today()
        fecha_inicio = fecha_fin.replace(day=1)

    fecha_inicio = parse_date(str(fecha_inicio))
    fecha_fin = parse_date(str(fecha_fin))

    ventas = Venta.objects.filter(fecha_hora_venta__date__range=[fecha_inicio, fecha_fin])

    context = {
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'clientes_por_dia': Cliente.objects.filter(fecha_alta__range=[fecha_inicio, fecha_fin])
            .values('fecha_alta').annotate(total=Count('id_cliente')),
        'total_ventas': ventas.count(),
        'total_tarjeta': ventas.filter(forma_de_pago='TARJETA')
            .aggregate(total=Sum('detalleventa__precio_total'))['total'] or 0,
    }

    return render(request, 'entidades/dashboard.html', context)
