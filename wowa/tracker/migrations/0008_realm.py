# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_characteritem_renaming_related_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=350, null=True, verbose_name='Realm Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
