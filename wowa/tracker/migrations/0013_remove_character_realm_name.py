# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_character_realm_add_connections'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='realm_name',
        ),
    ]
