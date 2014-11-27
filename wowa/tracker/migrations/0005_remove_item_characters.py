# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_copy_item_to_characteritem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='characters',
        ),
    ]
