# Generated by Django 3.1 on 2020-11-14 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celu', '0010_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='Tipo',
        ),
    ]