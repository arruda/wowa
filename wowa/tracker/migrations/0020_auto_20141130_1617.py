# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0019_characteritempriceondate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realmitempriceondate',
            options={'ordering': ['-date']},
        ),
    ]
