# Generated by Django 4.1.7 on 2024-03-12 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0032_remove_lineaconfigurador_articles_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion1',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion10',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion11',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion12',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion13',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion14',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion2',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion3',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion4',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion5',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion6',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion7',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion8',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='opcion9',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor1',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor10',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor11',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor12',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor13',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor14',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor2',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor3',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor4',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor5',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor6',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor7',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor8',
        ),
        migrations.RemoveField(
            model_name='configurationobject',
            name='valor9',
        ),
        migrations.CreateModel(
            name='ConfigurationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuration_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.configurationobject')),
                ('opcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.opcion')),
                ('valor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.valor')),
            ],
            options={
                'unique_together': {('configuration_object', 'opcion')},
            },
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opciones_y_valores',
            field=models.ManyToManyField(through='server.ConfigurationOption', to='server.valor'),
        ),
    ]
