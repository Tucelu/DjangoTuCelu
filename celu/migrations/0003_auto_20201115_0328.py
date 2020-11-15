# Generated by Django 3.1 on 2020-11-15 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('celu', '0002_auto_20201115_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='Detalle_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='celu.detalleproducto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalleproducto',
            name='Cliente_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalleproducto',
            name='Producto_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='celu.detalleproducto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='Tipo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='celu.tipo'),
            preserve_default=False,
        ),
    ]
