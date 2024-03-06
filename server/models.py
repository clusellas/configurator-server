import uuid

from django.db import models

# Create your models here.

from django.db import models


class Design(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, default='')

class Eje(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='eje', default='default.png')

class Ancho(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=50, default='')

class Coleccion(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, default='')
    img = models.ImageField(upload_to='coleccion', default='default.png')

class DesignColeccion(models.Model):
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='design_coleccion', default='default.png')

class Valor(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Valor', default='default.png')

class Opcion(models.Model):
    orden = models.IntegerField()
    name = models.CharField(max_length=50)
    valores = models.ManyToManyField(Valor)


class Articles(models.Model):
    CodigoEmpresa = models.SmallIntegerField()
    CodigoArticulo = models.CharField(max_length=50, unique=True)
    DescripcionArticulo = models.CharField(max_length=200)
    CodigoFamilia = models.CharField(max_length=10)
    CodigoSubfamilia = models.CharField(max_length=10)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
    design = models.ForeignKey(Design, on_delete=models.CASCADE)

    design_coleccion = models.ForeignKey(DesignColeccion, on_delete=models.CASCADE)
    ancho = models.ForeignKey(Ancho, on_delete=models.CASCADE)
    eje = models.ForeignKey(Eje, on_delete=models.CASCADE)
    visible = models.BooleanField(default=False)

class LineaConfigurador(models.Model):
    price = models.CharField(max_length=10)
    standard = models.BooleanField(default=False)
    opciones = models.ManyToManyField(Opcion, through='lineaOpcion')
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
class LineaOpcion(models.Model):
    linea = models.ForeignKey(LineaConfigurador, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE)


class ConfigurationObject(models.Model):
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, null=True)
    design = models.ForeignKey(Design, on_delete=models.CASCADE, null=True)
    ancho = models.ForeignKey(Ancho, on_delete=models.CASCADE, null=True)
    eje = models.ForeignKey(Eje, on_delete=models.CASCADE, null=True)

    articulo = models.ForeignKey(Articles, on_delete=models.CASCADE)
    current_linea = models.ForeignKey(LineaConfigurador, on_delete=models.CASCADE, null=True)

    opcion1 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj1', null=True)
    opcion2 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj2', null=True)
    opcion3 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj3', null=True)
    opcion4 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj4', null=True)
    opcion5 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj5', null=True)
    opcion6 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj6', null=True)
    opcion7 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj7', null=True)
    opcion8 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj8', null=True)
    opcion9 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj9', null=True)
    opcion10 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj10', null=True)
    opcion11 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj11', null=True)
    opcion12 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj12', null=True)
    opcion13 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj13', null=True)
    opcion14 = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='obj14', null=True)

    valor1 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value1', null=True)
    valor2 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value2', null=True)
    valor3 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value3', null=True)
    valor4 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value4', null=True)
    valor5 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value5', null=True)
    valor6 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value6', null=True)
    valor7 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value7', null=True)
    valor8 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value8', null=True)
    valor9 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value9', null=True)
    valor10 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value10', null=True)
    valor11 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value11', null=True)
    valor12 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value12', null=True)
    valor13 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value13', null=True)
    valor14 = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='obj_value14', null=True)

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

# class Option(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='images/')
#
# class Question(models.Model):
#     Question = models.CharField(max_length=100)
#     Options = models.ManyToManyField(Option)
#
# class Object(models.Model):
#     coleccion = models.CharField(max_length=5)
#     ancho = models.DecimalField(max_digits=28, decimal_places=10)
#     alto = models.DecimalField(max_digits=28, decimal_places=10)
#     distribucion_cajones = models.DecimalField(max_digits=28, decimal_places=10)
#     eje = models.CharField(max_length=5)
#
# class Render(models.Model):
#     imagen_ahora = models.ImageField(upload_to='images/')
#     objeto = models.ForeignKey(Object, on_delete=models.CASCADE)
#     preguntas = models.ManyToManyField(Question)
