# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0010_userprofile_active_beta'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetaSignup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
