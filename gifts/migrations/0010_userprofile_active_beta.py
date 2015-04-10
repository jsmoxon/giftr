# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0009_auto_20150402_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='active_beta',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
    ]
