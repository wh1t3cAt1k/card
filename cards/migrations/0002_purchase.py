# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_date', models.DateTimeField(verbose_name='Purchase Date')),
                ('item', models.CharField(max_length=255, verbose_name='Item name')),
                ('price', models.DecimalField(decimal_places=2, verbose_name='Item price', max_digits=10)),
                ('card', models.ForeignKey(verbose_name='Card used to purchase', to='cards.Card')),
            ],
        ),
    ]
