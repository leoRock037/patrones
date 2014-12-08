# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpiApp', '0002_remove_indicador_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='fuente',
            field=models.CharField(max_length=20, choices=[(b'Arial', b'Ar'), (b'Verdana', b'Ve')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='posicion',
            field=models.CharField(max_length=20, choices=[(b'Derecha', b'Der'), (b'Izquierda', b'Izq')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='tamano',
            field=models.CharField(max_length=20, choices=[(b'Pequeno', b'Pe.'), (b'Mediano', b'Md.'), (b'Grande', b'Gr.')]),
            preserve_default=True,
        ),
    ]
