# Generated by Django 3.1 on 2020-11-14 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('celu', '0020_remove_producto_sistemaoperativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo',
            name='Producto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='celu.producto'),
            preserve_default=False,
        ),
    ]
