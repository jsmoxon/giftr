# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0003_gift_price_cap'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='gift_selected',
            field=models.ForeignKey(related_name='selected_gift_option', blank=True, to='gifts.GiftOption', null=True),
            preserve_default=True,
        ),
    ]
