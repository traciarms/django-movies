# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20150804_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='rating',
            name='ratings',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rating',
            name='timestamp',
            field=models.IntegerField(),
        ),
    ]
