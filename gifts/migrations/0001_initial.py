# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('occasion', models.CharField(max_length=1000, null=True, blank=True)),
                ('target_arrival_date', models.DateField(null=True, blank=True)),
                ('start_process_date', models.DateField(auto_now_add=True)),
                ('ship_to_address', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GiftDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('occasion_date', models.DateField()),
                ('send_gift_option_email_date', models.DateField(null=True, blank=True)),
                ('occasion', models.CharField(max_length=1000, null=True, blank=True)),
                ('gift', models.ForeignKey(blank=True, to='gifts.Gift', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GiftDateStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GiftOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('selected', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=1000, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('photo_url', models.URLField(max_length=300, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('price', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GiftStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, null=True, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('favorites', models.TextField(null=True, blank=True)),
                ('gender', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recipient',
            name='user',
            field=models.ForeignKey(blank=True, to='gifts.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='giftdate',
            name='recipient',
            field=models.ForeignKey(to='gifts.Recipient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='giftdate',
            name='status',
            field=models.ForeignKey(blank=True, to='gifts.GiftDateStatus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gift',
            name='gift_options',
            field=models.ManyToManyField(to='gifts.GiftOption', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gift',
            name='recipient',
            field=models.ForeignKey(to='gifts.Recipient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gift',
            name='status',
            field=models.ForeignKey(blank=True, to='gifts.GiftStatus', null=True),
            preserve_default=True,
        ),
    ]
