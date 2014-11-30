# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_character_renaming_real_realmname'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='realm',
            field=models.ForeignKey(related_name='characters', to='tracker.Realm', null=True),
            preserve_default=True,
        ),
    ]
