# Generated by Django 4.1.7 on 2024-02-12 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_objeto_opcion_remove_render_age_remove_render_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Opcion',
        ),
        migrations.RemoveField(
            model_name='render',
            name='Objects',
        ),
        migrations.DeleteModel(
            name='Objeto',
        ),
        migrations.DeleteModel(
            name='Render',
        ),
    ]