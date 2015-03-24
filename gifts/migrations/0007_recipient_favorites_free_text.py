# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0006_gift_admin_send_gift_option_email_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='favorites_free_text',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
