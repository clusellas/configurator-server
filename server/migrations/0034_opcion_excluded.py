# Generated by Django 4.1.7 on 2024-03-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0033_remove_configurationobject_opcion1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opcion',
            name='excluded',
            field=models.BooleanField(default=False),
        ),
    ]