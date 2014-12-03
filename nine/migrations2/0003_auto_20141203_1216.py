# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nine', '0002_auto_20141203_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='nickname',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
