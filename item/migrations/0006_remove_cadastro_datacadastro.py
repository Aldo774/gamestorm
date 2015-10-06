# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20150925_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='datacadastro',
        ),
    ]
