# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('movie_id', models.TextField()),
                ('title', models.TextField()),
                ('genre', models.TextField()),
                ('tag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('ratings', models.TextField()),
                ('ave_rating', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('movie_id', models.ForeignKey(to='app1.Movie')),
                ('rater_id', models.ForeignKey(to='app1.Rater')),
            ],
        ),
    ]
