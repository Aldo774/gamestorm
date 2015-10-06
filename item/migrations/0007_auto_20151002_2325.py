# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_remove_cadastro_datacadastro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vis',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cadastropf',
            options={'ordering': ['nome'], 'verbose_name_plural': 'Cadastros Pessoas Fisicas', 'verbose_name': 'Cadastro Pessoa Fisica'},
        ),
        migrations.AlterModelOptions(
            name='cadastropj',
            options={'ordering': ['razaoSocial'], 'verbose_name_plural': 'Cadastros Pessoas Juridicas', 'verbose_name': 'Cadastro Pessoa Juridica'},
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='tipopessoa',
            field=models.CharField(choices=[('PF', 'Pessoa Fisica'), ('PJ', 'Pessoa Juridica')], null='True', verbose_name='Tipo', max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cadastropj',
            name='razaoSocial',
            field=models.CharField(max_length=100, verbose_name='Razao Social'),
        ),
        migrations.AlterField(
            model_name='item',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Data de Publicacao'),
        ),
        migrations.AddField(
            model_name='vis',
            name='itm',
            field=models.ForeignKey(to='item.Item'),
        ),
        migrations.AddField(
            model_name='vis',
            name='usu',
            field=models.ForeignKey(to='item.Cadastro', null=True),
        ),
    ]
