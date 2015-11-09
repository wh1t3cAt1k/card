# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('series', models.CharField(verbose_name='Series', max_length=8)),
                ('number', models.CharField(verbose_name='Number', max_length=16)),
                ('issue_date', models.DateTimeField(verbose_name='Issue Date', auto_now=True)),
                ('expire_date', models.DateTimeField(verbose_name='Expiry Date')),
                ('status', models.CharField(verbose_name='Status', max_length=3, default='AC')),
            ],
        ),
    ]
