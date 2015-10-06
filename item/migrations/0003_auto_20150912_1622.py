# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20150912_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Data de Publicação', default=datetime.datetime(2015, 9, 12, 19, 22, 22, 428664, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='visu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='qtd',
            field=models.IntegerField(default=0),
        ),
    ]
