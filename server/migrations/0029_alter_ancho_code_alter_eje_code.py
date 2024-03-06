# Generated by Django 4.1.7 on 2024-03-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0028_alter_eje_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ancho',
            name='code',
            field=models.IntegerField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='eje',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
