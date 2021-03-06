# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-06 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branding', '0005_organization_email_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='main_unsubscribe_url',
            field=models.URLField(blank=True, help_text=b"URL of page where user can submit their email address to be unsubscribed from organization's main email list", verbose_name=b'Main list unsubscribe URL'),
        ),
    ]
