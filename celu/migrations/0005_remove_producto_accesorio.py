# Generated by Django 3.1 on 2020-11-14 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celu', '0004_auto_20201114_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='Accesorio',
        ),
    ]
