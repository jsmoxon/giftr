# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0004_gift_gift_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='note_to_recipient',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
