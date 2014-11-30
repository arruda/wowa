# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_copy_character_realm_to_realm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='realm',
            new_name='realm_name',
        ),
    ]
