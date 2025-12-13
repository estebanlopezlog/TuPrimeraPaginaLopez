from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Producto, Cliente, Sucursal, Vendedor, Venta, DetalleVenta
from .forms import (
    ProductoForm, ClienteForm, SucursalForm, VendedorForm,
    VentaForm, DetalleVentaForm
)


# Pagina Principal
def index(request):
    return render(request, 'entidades/index.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'entidades/productos.html', {'productos': productos})
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'entidades/clientes.html', {'clientes': clientes})
def sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'entidades/sucursales.html', {'sucursales': sucursales})
def vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'entidades/vendedores.html', {'vendedores': vendedores})
def ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'entidades/ventas.html', {'ventas': ventas})
def quien_soy(request):
    return render(request, 'entidades/quien_soy.html')


# Formularios para Entidades
def nuevo_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('productos')
    return render(request, 'entidades/form_producto.html', {'form': form, 'titulo': 'Nuevo Producto'})
def nuevo_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes')
    return render(request, 'entidades/form_cliente.html', {'form': form, 'titulo': 'Nuevo Cliente'})
def nueva_sucursal(request):
    form = SucursalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sucursales')
    return render(request, 'entidades/form_sucursal.html', {'form': form, 'titulo': 'Nueva Sucursal'})
def nuevo_vendedor(request):
    form = VendedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vendedores')
    return render(request, 'entidades/form_vendedor.html', {'form': form, 'titulo': 'Nuevo Vendedor'})


# Formulario para Registrar Nueva Venta con Detalles
DetalleVentaFormSet = modelformset_factory(DetalleVenta, form=DetalleVentaForm, extra=5)

def nueva_venta(request):
    form = VentaForm(request.POST or None)
    formset = DetalleVentaFormSet(request.POST or None, queryset=DetalleVenta.objects.none())

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            venta = form.save()  # Guarda venta
            print("✅ Venta creada:", venta.id_venta)  #DEBUG

            for detalle_form in formset:
                if detalle_form.cleaned_data:
                    detalle = detalle_form.save(commit=False)
                    detalle.venta = venta
                    detalle.precio_total = (
                        detalle.cantidad_vendida * detalle.producto.precio_unitario
                    )
                    detalle.save()

            return redirect('ventas')  # Redirige al listado de ventas
        else:
            # Debugging de errores
            print("❌ Formulario no válido")
            print("Errores en VentaForm:", form.errors)
            print("Errores en DetalleVentaFormSet:", formset.errors)

    return render(request, 'entidades/form_venta.html', {
        'form': form,
        'formset': formset,
        'titulo': 'Registrar Nueva Venta'
    })


