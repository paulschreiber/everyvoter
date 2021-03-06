# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-12 16:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_smalluuid.models
import everyvoter_common.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', django_smalluuid.models.SmallUUIDField(db_index=True, default=django_smalluuid.models.UUIDDefault(), editable=False, unique=True)),
                ('daily_batch_sample', models.BooleanField(verbose_name=b'Sample All Emails Daily', default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notification Setting',
                'verbose_name_plural': 'Notification Settings',
            },
            bases=(everyvoter_common.utils.models.CacheMixinModel, models.Model),
        ),
    ]
