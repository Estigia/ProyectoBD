# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 02:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Registros', '0002_auto_20160421_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='Victima_id',
        ),
        migrations.AddField(
            model_name='registro',
            name='apellidos',
            field=models.CharField(default='xx', max_length=55),
        ),
        migrations.AddField(
            model_name='registro',
            name='cui',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='registro',
            name='edad',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registro',
            name='muerto',
            field=models.BooleanField(default=datetime.datetime(2016, 4, 21, 2, 13, 51, 287864, tzinfo=utc), null=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='nombres',
            field=models.CharField(default='xx', max_length=55),
        ),
        migrations.AddField(
            model_name='registro',
            name='profesion',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='registro',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('D', 'Desconocido')], default='D', max_length=2),
        ),
        migrations.DeleteModel(
            name='Victima',
        ),
    ]
