# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0018_auto_20141130_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterItemPriceOnDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Date')),
                ('avg_price', models.DecimalField(default=b'0.0', verbose_name='Average Price', max_digits=10, decimal_places=2)),
                ('character', models.ForeignKey(related_name='character_item_prices_on_date', to='tracker.Character', null=True)),
                ('item', models.ForeignKey(related_name='character_item_prices_on_date', to='tracker.Item', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
