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
    excluded = models.BooleanField(default=False)
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
    opciones_y_valores = models.ManyToManyField(Valor, through='ConfigurationOption')

    def fill_from_linea(self):
        if self.current_linea:
            # Clear existing configuration options
            self.opciones_y_valores.clear()

            # Get all option-value pairs from current_linea
            option_value_pairs = self.current_linea.lineaopcion_set.select_related('opcion', 'valor')

            # Create ConfigurationOption instances
            configuration_options = [
                ConfigurationOption(configuration_object=self, opcion=pair.opcion, valor=pair.valor)
                for pair in option_value_pairs
            ]

            # Bulk create the configuration options
            ConfigurationOption.objects.bulk_create(configuration_options)
            self.save()

    def update_option_value(self, opcion, new_valor):
        # Check if the provided option belongs to the current linea
        if opcion in self.current_linea.opciones.all():
            # Update the value of the provided option
            ConfigurationOption.objects.filter(configuration_object=self, opcion=opcion).update(valor=new_valor)

            # Get all option-value pairs of the current configuration
            current_configuration =  ConfigurationOption.objects.filter(configuration_object=self, opcion__excluded=False)

            # Get all excluded options
            excluded_options = Opcion.objects.filter(excluded=True)
            if opcion in excluded_options:
                return
            # Find the linea that matches the updated configuration exactly
            for linea in LineaConfigurador.objects.filter(coleccion=self.coleccion):
                linea_options = linea.lineaopcion_set.select_related('opcion', 'valor')
                #if len(linea_options) != len(current_configuration):
                #    continue  # Skip if the number of options differs

                # Check if all non-excluded options match
                all = False
                for pair in linea_options:
                    if (pair.opcion.id, pair.valor.id) in current_configuration.values_list('opcion', 'valor') or pair.opcion in excluded_options:
                      all = True
                    else:
                        all = False
                        break
                if all:
                    self.current_linea = linea
                    self.save()
                    self.fill_from_linea()
                    return


class ConfigurationOption(models.Model):
    configuration_object = models.ForeignKey(ConfigurationObject, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('configuration_object', 'opcion')

    def save(self, *args, **kwargs):
        # Ensure that the option and value belong to the same linea
        if self.opcion in self.configuration_object.current_linea.opciones.all():
            super(ConfigurationOption, self).save(*args, **kwargs)

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
