# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='checkout',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
