# Generated by Django 4.1.7 on 2024-02-09 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoArticulo', models.CharField(max_length=100)),
                ('Coleccion', models.CharField(max_length=100)),
                ('Ancho', models.IntegerField()),
                ('ConfiguracionCajones', models.CharField(max_length=100)),
                ('Eje', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Valor', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='render',
            name='age',
        ),
        migrations.RemoveField(
            model_name='render',
            name='name',
        ),
        migrations.AddField(
            model_name='render',
            name='Json',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='render',
            name='User',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='render',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='render',
            name='Objects',
            field=models.ManyToManyField(to='server.objeto'),
        ),
    ]