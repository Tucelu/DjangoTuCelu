# Generated by Django 3.1 on 2020-11-14 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celu', '0019_auto_20201114_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='sistemaoperativo',
        ),
    ]