# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0012_betasignup_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='betasignup',
            name='creation',
            field=models.DateField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
