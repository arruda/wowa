# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_rename_item_characters_m2m_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteritem',
            name='character',
            field=models.ForeignKey(related_name='character_items', to='tracker.Character'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='characteritem',
            name='item',
            field=models.ForeignKey(related_name='character_items', to='tracker.Item'),
            preserve_default=True,
        ),
    ]
