# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-10 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authc', models.CharField(max_length=10)),
                ('count', models.IntegerField(default=0)),
                ('mail', models.CharField(max_length=10)),
                ('rmail', models.CharField(max_length=10)),
            ],
        ),
    ]
