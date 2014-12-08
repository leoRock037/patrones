# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('metrica', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('tamano', models.CharField(max_length=7, choices=[(b'Pequeno', b'Pe.'), (b'Mediano', b'Md.'), (b'Grande', b'Gr.')])),
                ('txt_color', models.CharField(max_length=100)),
                ('fuente', models.CharField(max_length=7, choices=[(b'Arial', b'Ar'), (b'Verdana', b'Ve')])),
                ('logo_url', models.CharField(max_length=500)),
                ('posicion', models.CharField(max_length=7, choices=[(b'Derecha', b'Der'), (b'Izquierda', b'Izq')])),
                ('indicadores', models.ManyToManyField(to='kpiApp.Indicador')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='organizacion',
            name='representante',
            field=models.ForeignKey(to='kpiApp.Representante'),
            preserve_default=True,
        ),
    ]
