# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Armas', '0003_auto_20160419_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arma',
            name='categoria',
            field=models.CharField(choices=[('Fg', 'Arma de Fuego'), ('Bn', 'Arma Blanca'), ('Ot', 'Otro')], default='Ot', max_length=2),
        ),
    ]