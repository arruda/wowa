# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_remove_item_characters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='characters_new',
        ),
        migrations.AddField(
            model_name='item',
            name='characters',
            field=models.ManyToManyField(related_name='items', null=True, through='tracker.CharacterItem', to='tracker.Character', blank=True),
            preserve_default=True,
        ),
    ]
