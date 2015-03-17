# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0005_gift_note_to_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='admin_send_gift_option_email_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
