# Generated by Django 3.1 on 2020-12-05 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('celu', '0029_carrito_detalle_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleproducto',
            name='Producto_id',
        ),
        migrations.AddField(
            model_name='producto',
            name='detalle_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='celu.detalleproducto'),
        ),
    ]
