# Generated by Django 4.1.7 on 2024-02-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_alter_articles_codigodepartamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='CodigoDivisa',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='articles',
            name='CodigoFamilia',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='articles',
            name='CodigoSubfamilia',
            field=models.CharField(max_length=10),
        ),
    ]
