# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('imagem', models.ImageField(upload_to='imagens/item/')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('qtd', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nome_plataforma', models.CharField(max_length=30)),
                ('imagem', models.ImageField(upload_to='imagens/plataforma')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='n_plataforma',
            field=models.ForeignKey(to='item.Plataforma'),
        ),
    ]
