# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0008_auto_20150402_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftoption',
            name='favorite_tags',
            field=models.ManyToManyField(to='gifts.FavoriteTag', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipient',
            name='favorite_tags',
            field=models.ManyToManyField(to='gifts.FavoriteTag', null=True, blank=True),
            preserve_default=True,
        ),
    ]
