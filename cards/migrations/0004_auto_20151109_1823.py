# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20151109_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.CharField(choices=[('AC', 'Active'), ('EX', 'Expired'), ('DE', 'Deactivated')], default='AC', verbose_name='Status', max_length=2),
        ),
    ]
