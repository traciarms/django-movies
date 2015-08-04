# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_id',
            new_name='imdb_id',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='rater_id',
            new_name='rater',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='user_id',
        ),
        migrations.AddField(
            model_name='movie',
            name='tmdb_id',
            field=models.TextField(default=datetime.datetime(2015, 8, 3, 23, 5, 17, 261350, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
