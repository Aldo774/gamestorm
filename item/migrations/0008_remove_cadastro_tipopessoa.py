# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_auto_20151002_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='tipopessoa',
        ),
    ]
