# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpiApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpi',
            name='organizacion',
            field=models.ManyToManyField(to='kpiApp.Organizacion'),
            preserve_default=True,
        ),
    ]
