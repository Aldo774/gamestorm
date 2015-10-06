# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20150912_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='plataforma',
            name='pagina',
            field=models.CharField(default='/item/', max_length=30),
        ),
        migrations.AlterField(
            model_name='item',
            name='imagem',
            field=models.ImageField(upload_to='item'),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='imagem',
            field=models.ImageField(upload_to='plataforma'),
        ),
    ]
