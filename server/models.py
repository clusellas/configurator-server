import uuid

from django.db import models

# Create your models here.

from django.db import models


class Articles(models.Model):
    CodigoEmpresa = models.SmallIntegerField()
    CodigoArticulo = models.CharField(max_length=50)
    DescripcionArticulo = models.CharField(max_length=200)
    Descripcion2Articulo = models.CharField(max_length=40)
    DescripcionLinea = models.TextField()
    ComentarioArticulo = models.TextField()
    MarcaProducto = models.CharField(max_length=89)
    CodigoAlternativo = models.CharField(max_length=20)
    CodigoAlternativo2 = models.CharField(max_length=20)
    CodigoArticuloOferta = models.CharField(max_length=20)
    CodigoArancelario = models.CharField(max_length=12)
    CodigoProveedor = models.CharField(max_length=15)
    ReferenciaEdi = models.CharField(max_length=35)
    PublicarInternet = models.SmallIntegerField()
    TipoArticulo = models.CharField(max_length=1)
    Utilizado = models.SmallIntegerField()
    FechaAlta = models.DateTimeField(null=True)
    Temporada = models.CharField(max_length=50)
    CodigoFamilia = models.CharField(max_length=10)
    CodigoSubfamilia = models.CharField(max_length=10)
    CodigoDivisa = models.CharField(max_length=5)
    CodigoProyecto = models.CharField(max_length=13)
    CodigoSeccion = models.CharField(max_length=14)
    CodigoDepartamento = models.CharField(max_length=15)
    CodigoDefinicion = models.CharField(max_length=15)
    Colores = models.SmallIntegerField(default=None, blank=True, null=True)
    IvaIncluido = models.SmallIntegerField()
    PrecioCompra = models.DecimalField(max_digits=28, decimal_places=10)
    PrecioVenta = models.DecimalField(max_digits=28, decimal_places=10)
    PrecioVentaconIVA1 = models.DecimalField(max_digits=28, decimal_places=10)
    PrecioVentaconIVA2 = models.DecimalField(max_digits=28, decimal_places=10)
    PrecioVentaconIVA3 = models.DecimalField(max_digits=28, decimal_places=10)
    PrecioVentasinIVA1 = models.DecimalField(max_digits=28, decimal_places=10)
    PrecioVentasinIVA2 = models.DecimalField(max_digits=28, decimal_places=10)
    PrecioVentasinIVA3 = models.DecimalField(max_digits=28, decimal_places=10)
    PrecioOfertaconIVA = models.DecimalField(max_digits=28, decimal_places=10)
    PrecioOfertasinIVA = models.DecimalField(max_digits=28, decimal_places=10)
    PesoBrutoUnitario = models.DecimalField(max_digits=28, decimal_places=10)
    PesoNetoUnitario = models.DecimalField(max_digits=28, decimal_places=10)
    VolumenUnitario = models.DecimalField(max_digits=28, decimal_places=10)


class ConfiguradorMobiliario(models.Model):
    CodigoFamilia = models.CharField(max_length=10)
    CodigoSubfamilia = models.CharField(max_length=10)
    NombrePantalla = models.CharField(max_length=50)
    NombreOpcion1 = models.CharField(max_length=20)
    Opcion1 = models.CharField(max_length=15)
    NombreOpcion2 = models.CharField(max_length=20)
    Opcion2 = models.CharField(max_length=15)
    ColumnaPrecio = models.SmallIntegerField()
    NombreOpcion3 = models.CharField(max_length=20)
    Opcion3 = models.CharField(max_length=15)
    NombreOpcion4 = models.CharField(max_length=20)
    Opcion4 = models.CharField(max_length=15)
    NombreOpcion5 = models.CharField(max_length=20)
    Opcion5 = models.CharField(max_length=15)
    NombreOpcion6 = models.CharField(max_length=20)
    Opcion6 = models.CharField(max_length=15)
    NombreOpcion7 = models.CharField(max_length=20)
    Opcion7 = models.CharField(max_length=15)
    NombreOpcion8 = models.CharField(max_length=20)
    Opcion8 = models.CharField(max_length=15)
    NombreOpcion9 = models.CharField(max_length=20)
    Opcion9 = models.CharField(max_length=15)
    NombreAncho = models.CharField(max_length=20)
    OpcionAncho = models.CharField(max_length=15)
    NombreFondo = models.CharField(max_length=20)
    OpcionFondo = models.CharField(max_length=15)
    NombreAlto = models.CharField(max_length=20)
    OpcionAlto = models.CharField(max_length=15)
    NombreInterior = models.CharField(max_length=20)
    OpcionInterior = models.CharField(max_length=15)
    NombreOpcion10 = models.CharField(max_length=20)
    Opcion10 = models.CharField(max_length=15)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['CodigoFamilia', 'CodigoSubfamilia', 'Opcion1', 'Opcion2', 'Opcion4', 'Opcion6'],
                name='ConfiguradorMobiliario_PK_CM'
                )
        ]

class Colors(models.Model):
    CodigoEmpresa = models.SmallIntegerField()
    NombreOpcion = models.CharField(max_length=20)
    CodigoColor = models.CharField(max_length=10)
    Color = models.CharField(max_length=35)
    IdColor = models.UUIDField(default=uuid.uuid4, unique=False)
    DescripcionWeb = models.CharField(max_length=30)
    Orden = models.SmallIntegerField()
    ColorFRA = models.CharField(max_length=35)
    ColorING = models.CharField(max_length=35)
    ColorITA = models.CharField(max_length=35)
    ColorPROV = models.CharField(max_length=100)
    CodigoColorAbreviado = models.CharField(max_length=4)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['CodigoEmpresa', 'CodigoColor', 'NombreOpcion'],
                name='Colores'
            )
        ]

class Option(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

class Question(models.Model):
    Question = models.CharField(max_length=100)
    Options = models.ManyToManyField(Option)





