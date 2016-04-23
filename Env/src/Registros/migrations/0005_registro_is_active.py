# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registros', '0004_auto_20160421_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='is_active',
            field=models.BooleanField(default=None),
        ),
    ]
