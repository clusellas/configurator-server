# Generated by Django 4.1.7 on 2024-02-12 14:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors',
            name='IdColor',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
