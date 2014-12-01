# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0020_auto_20141130_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characteritempriceondate',
            options={'ordering': ['-date']},
        ),
    ]
