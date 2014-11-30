# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_remove_character_realm_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealmItemPriceOnDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date', null=True)),
                ('item', models.ForeignKey(related_name='item_prices_on_date', to='tracker.Item', null=True)),
                ('realm', models.ForeignKey(related_name='item_prices_on_date', to='tracker.Realm', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
