# Generated by Django 4.1.7 on 2024-02-19 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0018_alter_coleccion_default_ancho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleccion',
            name='default_ancho',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.ancho'),
        ),
        migrations.AlterField(
            model_name='coleccion',
            name='default_design',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.design'),
        ),
        migrations.AlterField(
            model_name='coleccion',
            name='default_eje',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.eje'),
        ),
    ]
