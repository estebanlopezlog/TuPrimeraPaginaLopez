from django.db import models

# Create your models here.


from django.db import models


# TABLAS MAESTRAS

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_producto} (${self.precio_unitario})"


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=10, unique=True)
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=150)
    codigo_postal = models.CharField(max_length=10)
    localidad = models.CharField(max_length=100)
    fecha_alta = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_cliente} {self.apellido_cliente}"


class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre_sucursal = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_sucursal


class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key=True)
    nombre_vendedor = models.CharField(max_length=100)
    apellido_vendedor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_vendedor} {self.apellido_vendedor}"



# TABLA DE HECHOS

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_hora_venta = models.DateTimeField(auto_now_add=True)
    
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    producto = models.ManyToManyField(Producto, through='DetalleVenta')

    forma_de_pago = models.CharField(
    max_length=50,
    choices=[
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('TRANSFERENCIA', 'Transferencia')
    ],
    blank=False,  #obligatorio
    null=False
)


    def __str__(self):
        return f"Venta #{self.id_venta} - {self.cliente.nombre_cliente} ({self.fecha_hora_venta.strftime('%d/%m/%Y')})"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_vendida = models.IntegerField()
    precio_total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre_producto} x {self.cantidad_vendida}"
    

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        default='profile_pics/default.jpg',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Perfil de {self.user.username}"
