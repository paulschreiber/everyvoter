# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-13 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0008_specific_activity_idx'),
        ('blocks', '0002_email_blocks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='blocks',
        ),
        migrations.AddField(
            model_name='email',
            name='blocks',
            field=models.ManyToManyField(blank=True, to='blocks.Block'),
        ),
    ]
