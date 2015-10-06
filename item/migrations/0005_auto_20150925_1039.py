# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0004_auto_20150923_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('num', models.CharField(max_length=4)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=8)),
                ('pais', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=15)),
                ('tipopessoa', models.CharField(max_length=2, choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], null='True', verbose_name='Tipo', blank=True)),
                ('datacadastro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ddd', models.IntegerField()),
                ('telefone', models.CharField(max_length=20)),
                ('ramal', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CadastroPF',
            fields=[
                ('cadastro_ptr', models.OneToOneField(primary_key=True, auto_created=True, parent_link=True, serialize=False, to='item.Cadastro')),
                ('rg', models.CharField(max_length=9, null=True, blank=True)),
                ('cpf', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Cadastros Pessoas Físicas',
                'verbose_name': 'Cadastro Pessoa Física',
                'ordering': ['nome'],
            },
            bases=('item.cadastro',),
        ),
        migrations.CreateModel(
            name='CadastroPJ',
            fields=[
                ('cadastro_ptr', models.OneToOneField(primary_key=True, auto_created=True, parent_link=True, serialize=False, to='item.Cadastro')),
                ('razaoSocial', models.CharField(max_length=100, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name_plural': 'Cadastros Pessoas Jurídicas',
                'verbose_name': 'Cadastro Pessoa Jurídica',
                'ordering': ['razaoSocial'],
            },
            bases=('item.cadastro',),
        ),
        migrations.AddField(
            model_name='telefone',
            name='cadastro',
            field=models.ForeignKey(to='item.Cadastro'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='user',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]
