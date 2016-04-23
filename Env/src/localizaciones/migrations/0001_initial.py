# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('departamento', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('municipio', models.CharField(max_length=45)),
                ('Departamento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localizaciones.Departamento')),
            ],
        ),
    ]
