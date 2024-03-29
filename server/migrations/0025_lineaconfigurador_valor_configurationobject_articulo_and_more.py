# Generated by Django 4.1.7 on 2024-03-06 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0024_remove_ancho_ejes_remove_coleccion_default_ancho_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaConfigurador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=10)),
                ('standard', models.BooleanField(default=False)),
                ('articles', models.ManyToManyField(related_name='lineasConfigurador', to='server.articles')),
            ],
        ),
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.png', upload_to='Valor')),
            ],
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='articulo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='server.articles'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('valores', models.ManyToManyField(to='server.valor')),
            ],
        ),
        migrations.CreateModel(
            name='LineaOpcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.lineaconfigurador')),
                ('opcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.opcion')),
                ('valor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.valor')),
            ],
        ),
        migrations.AddField(
            model_name='lineaconfigurador',
            name='opciones',
            field=models.ManyToManyField(through='server.LineaOpcion', to='server.opcion'),
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj1', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion10',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj10', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion11',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj11', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion12',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj12', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion13',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj13', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion14',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj14', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj2', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj3', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion4',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj4', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion5',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj5', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion6',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj6', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion7',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj7', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion8',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj8', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='opcion9',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj9', to='server.opcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value1', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor10',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value10', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor11',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value11', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor12',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value12', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor13',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value13', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor14',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value14', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value2', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value3', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor4',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value4', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor5',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value5', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor6',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value6', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor7',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value7', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor8',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value8', to='server.valor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configurationobject',
            name='valor9',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obj_value9', to='server.valor'),
            preserve_default=False,
        ),
    ]
