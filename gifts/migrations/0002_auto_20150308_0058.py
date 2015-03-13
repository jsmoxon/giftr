# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftdate',
            name='gift',
        ),
        migrations.RemoveField(
            model_name='giftdate',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='giftdate',
            name='status',
        ),
        migrations.DeleteModel(
            name='GiftDate',
        ),
        migrations.DeleteModel(
            name='GiftDateStatus',
        ),
        migrations.RenameField(
            model_name='gift',
            old_name='target_arrival_date',
            new_name='occasion_date',
        ),
        migrations.AddField(
            model_name='gift',
            name='send_gift_option_email_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
