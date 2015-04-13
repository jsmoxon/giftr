# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0014_betasignup_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='betasignup',
            name='created',
        ),
        migrations.RemoveField(
            model_name='betasignup',
            name='creation',
        ),
    ]
