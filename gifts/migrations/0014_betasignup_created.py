# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0013_betasignup_creation'),
    ]

    operations = [
        migrations.AddField(
            model_name='betasignup',
            name='created',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 4, 4, 28, 999058, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
