# Generated by Django 3.1 on 2020-11-15 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celu', '0027_auto_20201114_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_compra', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='detalleproducto',
            old_name='Total',
            new_name='Total_iva',
        ),
    ]
