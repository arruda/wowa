# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0014_realmitempriceondate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realmitempriceondate',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, auto_now_add=True, null=True, verbose_name='Date'),
            preserve_default=True,
        ),
    ]
