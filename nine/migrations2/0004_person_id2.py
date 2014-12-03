# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nine', '0003_auto_20141203_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='No',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
