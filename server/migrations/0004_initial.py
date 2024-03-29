# Generated by Django 4.1.7 on 2024-02-12 14:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('server', '0003_delete_opcion_remove_render_objects_delete_objeto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoEmpresa', models.SmallIntegerField()),
                ('CodigoArticulo', models.CharField(max_length=50)),
                ('DescripcionArticulo', models.CharField(max_length=200)),
                ('Descripcion2Articulo', models.CharField(max_length=40)),
                ('DescripcionLinea', models.TextField()),
                ('ComentarioArticulo', models.TextField()),
                ('MarcaProducto', models.CharField(max_length=89)),
                ('CodigoAlternativo', models.CharField(max_length=20)),
                ('CodigoAlternativo2', models.CharField(max_length=20)),
                ('CodigoArticuloOferta', models.CharField(max_length=20)),
                ('CodigoArancelario', models.CharField(max_length=12)),
                ('CodigoProveedor', models.CharField(max_length=15)),
                ('ReferenciaEdi', models.CharField(max_length=35)),
                ('PublicarInternet', models.SmallIntegerField()),
                ('TipoArticulo', models.CharField(max_length=1)),
                ('Utilizado', models.SmallIntegerField()),
                ('FechaAlta', models.DateTimeField(null=True)),
                ('Temporada', models.CharField(max_length=10)),
                ('CodigoFamilia', models.CharField(max_length=10)),
                ('CodigoSubfamilia', models.CharField(max_length=10)),
                ('CodigoDivisa', models.CharField(max_length=3)),
                ('CodigoProyecto', models.CharField(max_length=10)),
                ('CodigoSeccion', models.CharField(max_length=10)),
                ('CodigoDepartamento', models.CharField(max_length=10)),
                ('CodigoDefinicion', models.CharField(max_length=15)),
                ('Colores', models.SmallIntegerField()),
                ('IvaIncluido', models.SmallIntegerField()),
                ('PrecioCompra', models.DecimalField(decimal_places=10, max_digits=28)),
                ('PrecioVenta', models.DecimalField(decimal_places=10, max_digits=28)),
                ('PrecioVentaconIVA1', models.DecimalField(decimal_places=10, max_digits=28)),
                ('PrecioVentaconIVA2', models.DecimalField(decimal_places=10, max_digits=28)),
                ('PrecioVentaconIVA3', models.DecimalField(decimal_places=10, max_digits=28)),
                ('PrecioVentasinIVA1', models.DecimalField(decimal_places=10, max_digits=28)),
                ('PrecioVentasinIVA2', models.DecimalField(decimal_places=10, max_digits=28)),
                ('PrecioVentasinIVA3', models.DecimalField(decimal_places=10, max_digits=28)),
                ('PrecioOfertaconIVA', models.DecimalField(decimal_places=10, max_digits=28)),
                ('PrecioOfertasinIVA', models.DecimalField(decimal_places=10, max_digits=28)),
                ('PesoBrutoUnitario', models.DecimalField(decimal_places=10, max_digits=28)),
                ('PesoNetoUnitario', models.DecimalField(decimal_places=10, max_digits=28)),
                ('VolumenUnitario', models.DecimalField(decimal_places=10, max_digits=28)),
            ],
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoEmpresa', models.SmallIntegerField()),
                ('NombreOpcion', models.CharField(max_length=20)),
                ('CodigoColor', models.CharField(max_length=10)),
                ('Color', models.CharField(max_length=35)),
                ('IdColor', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('DescripcionWeb', models.CharField(max_length=30)),
                ('Orden', models.SmallIntegerField()),
                ('ColorFRA', models.CharField(max_length=35)),
                ('ColorING', models.CharField(max_length=35)),
                ('ColorITA', models.CharField(max_length=35)),
                ('ColorPROV', models.CharField(max_length=100)),
                ('CodigoColorAbreviado', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='ConfiguradorMobiliario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoFamilia', models.CharField(max_length=10)),
                ('CodigoSubfamilia', models.CharField(max_length=10)),
                ('NombrePantalla', models.CharField(max_length=50)),
                ('NombreOpcion1', models.CharField(max_length=20)),
                ('Opcion1', models.CharField(max_length=15)),
                ('NombreOpcion2', models.CharField(max_length=20)),
                ('Opcion2', models.CharField(max_length=15)),
                ('ColumnaPrecio', models.SmallIntegerField()),
                ('NombreOpcion3', models.CharField(max_length=20)),
                ('Opcion3', models.CharField(max_length=15)),
                ('NombreOpcion4', models.CharField(max_length=20)),
                ('Opcion4', models.CharField(max_length=15)),
                ('NombreOpcion5', models.CharField(max_length=20)),
                ('Opcion5', models.CharField(max_length=15)),
                ('NombreOpcion6', models.CharField(max_length=20)),
                ('Opcion6', models.CharField(max_length=15)),
                ('NombreOpcion7', models.CharField(max_length=20)),
                ('Opcion7', models.CharField(max_length=15)),
                ('NombreOpcion8', models.CharField(max_length=20)),
                ('Opcion8', models.CharField(max_length=15)),
                ('NombreOpcion9', models.CharField(max_length=20)),
                ('Opcion9', models.CharField(max_length=15)),
                ('NombreAncho', models.CharField(max_length=20)),
                ('OpcionAncho', models.CharField(max_length=15)),
                ('NombreFondo', models.CharField(max_length=20)),
                ('OpcionFondo', models.CharField(max_length=15)),
                ('NombreAlto', models.CharField(max_length=20)),
                ('OpcionAlto', models.CharField(max_length=15)),
                ('NombreInterior', models.CharField(max_length=20)),
                ('OpcionInterior', models.CharField(max_length=15)),
                ('NombreOpcion10', models.CharField(max_length=20)),
                ('Opcion10', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddConstraint(
            model_name='configuradormobiliario',
            constraint=models.UniqueConstraint(fields=('CodigoFamilia', 'CodigoSubfamilia', 'Opcion1', 'Opcion2', 'Opcion4', 'Opcion6'), name='ConfiguradorMobiliario_PK_CM'),
        ),
        migrations.AddConstraint(
            model_name='colors',
            constraint=models.UniqueConstraint(fields=('CodigoEmpresa', 'CodigoColor', 'NombreOpcion'), name='Colores'),
        ),
    ]
