# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20150803_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='imdb_id',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tmdb_id',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='ave_rating',
        ),
        migrations.AddField(
            model_name='rater',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='gender',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='occupation',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='zip_code',
            field=models.CharField(default=datetime.datetime(2015, 8, 4, 16, 30, 35, 490793, tzinfo=utc), max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='rating',
            name='ratings',
            field=models.FloatField(),
        ),
    ]
