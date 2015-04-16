# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0011_betasignup'),
    ]

    operations = [
        migrations.AddField(
            model_name='betasignup',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
