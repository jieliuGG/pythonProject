# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-06 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid1', models.IntegerField()),
                ('uid2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Swiped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(db_index=True, verbose_name='用户自身 id')),
                ('sid', models.IntegerField(db_index=True, verbose_name='被滑的陌生人 id')),
                ('mark', models.CharField(choices=[('like', '喜欢'), ('superlike', '喜欢'), ('dislike', '喜欢')], db_index=True, max_length=16, verbose_name='滑动类型')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='滑动的时间')),
            ],
            options={
                'ordering': ['-time', 'uid', 'sid'],
            },
        ),
    ]
