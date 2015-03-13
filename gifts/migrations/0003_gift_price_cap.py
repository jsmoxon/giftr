# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0002_auto_20150308_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='price_cap',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
