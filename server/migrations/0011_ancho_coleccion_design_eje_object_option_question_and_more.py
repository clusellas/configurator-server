# Generated by Django 4.1.7 on 2024-02-15 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_alter_articles_colores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ancho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Eje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coleccion', models.CharField(max_length=5)),
                ('ancho', models.DecimalField(decimal_places=10, max_digits=28)),
                ('alto', models.DecimalField(decimal_places=10, max_digits=28)),
                ('distribucion_cajones', models.DecimalField(decimal_places=10, max_digits=28)),
                ('eje', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=100)),
                ('Options', models.ManyToManyField(to='server.option')),
            ],
        ),
        migrations.RemoveField(
            model_name='articles',
            name='CodigoAlternativo',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='CodigoAlternativo2',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='CodigoArancelario',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='CodigoArticuloOferta',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='CodigoDefinicion',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='CodigoDepartamento',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='CodigoDivisa',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='CodigoProveedor',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='CodigoProyecto',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='CodigoSeccion',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='Colores',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='ComentarioArticulo',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='Descripcion2Articulo',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='DescripcionLinea',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='FechaAlta',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='IvaIncluido',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='MarcaProducto',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PesoBrutoUnitario',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PesoNetoUnitario',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PrecioCompra',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PrecioOfertaconIVA',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PrecioOfertasinIVA',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PrecioVenta',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PrecioVentaconIVA1',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PrecioVentaconIVA2',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PrecioVentaconIVA3',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PrecioVentasinIVA1',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PrecioVentasinIVA2',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PrecioVentasinIVA3',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='PublicarInternet',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='ReferenciaEdi',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='Temporada',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='TipoArticulo',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='Utilizado',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='VolumenUnitario',
        ),
        migrations.AlterField(
            model_name='articles',
            name='CodigoArticulo',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='Render',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_ahora', models.ImageField(upload_to='images/')),
                ('objeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.object')),
                ('preguntas', models.ManyToManyField(to='server.question')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='ancho',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='server.ancho'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='coleccion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='server.coleccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='design',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='server.design'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='eje',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='server.eje'),
            preserve_default=False,
        ),
    ]
