# Generated by Django 4.1.7 on 2024-03-06 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0030_alter_ancho_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='configurationobject',
            name='current_linea',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.lineaconfigurador'),
        ),
    ]