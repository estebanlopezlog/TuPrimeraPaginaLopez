
from django_select2.forms import Select2Widget

from django.forms import modelformset_factory
from .models import DetalleVenta
from django import forms
from .models import Producto, Cliente, Sucursal, Vendedor, Venta, DetalleVenta


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio_unitario', 'proveedor']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni', 'nombre_cliente', 'apellido_cliente', 'domicilio', 'codigo_postal', 'localidad']

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre_sucursal']

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre_vendedor', 'apellido_vendedor']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['vendedor', 'cliente', 'sucursal', 'forma_de_pago']

        widgets = {
            'vendedor': Select2Widget(attrs={'data-placeholder': 'Buscar vendedor...'}),
            'cliente': Select2Widget(attrs={'data-placeholder': 'Buscar cliente por nombre o DNI...'}),
        }


class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad_vendida']

DetalleVentaFormSet = modelformset_factory(
    DetalleVenta, form=DetalleVentaForm, extra=1, can_delete=True
)

