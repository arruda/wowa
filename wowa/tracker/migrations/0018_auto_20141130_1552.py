# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0017_realmitempriceondate_avg_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realmitempriceondate',
            name='item',
            field=models.ForeignKey(related_name='realm_item_prices_on_date', to='tracker.Item', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realmitempriceondate',
            name='realm',
            field=models.ForeignKey(related_name='realm_item_prices_on_date', to='tracker.Realm', null=True),
            preserve_default=True,
        ),
    ]
