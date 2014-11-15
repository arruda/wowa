# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=350, null=True, verbose_name='Character Name')),
                ('realm', models.CharField(max_length=350, null=True, verbose_name='Realm')),
                ('user', models.ForeignKey(related_name='characters', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blizzard_id', models.PositiveIntegerField(null=True, verbose_name='Blizzard Item Id')),
                ('name', models.CharField(max_length=350, null=True, verbose_name='Item Name', blank=True)),
                ('characters', models.ManyToManyField(related_name='items', null=True, to='tracker.Character', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
