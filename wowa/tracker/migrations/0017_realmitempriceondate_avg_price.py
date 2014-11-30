# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0016_auto_20141130_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='realmitempriceondate',
            name='avg_price',
            field=models.DecimalField(default=b'0.0', verbose_name='Average Price', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
