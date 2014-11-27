# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_characteritem'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='characters_new',
            field=models.ManyToManyField(related_name='items_new', null=True, through='tracker.CharacterItem', to='tracker.Character', blank=True),
            preserve_default=True,
        ),
    ]
