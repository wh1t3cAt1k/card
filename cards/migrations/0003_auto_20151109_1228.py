# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='issue_date',
            field=models.DateTimeField(verbose_name='Issue Date'),
        ),
    ]
