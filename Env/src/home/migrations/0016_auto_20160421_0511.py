# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20160421_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=254, unique=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre_usuario',
            field=models.CharField(max_length=20, unique=False),
        ),
    ]
