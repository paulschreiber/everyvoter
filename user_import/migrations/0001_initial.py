# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-25 04:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import kennedy_common.utils.models
import kennedy_common.utils.storages
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.TextField(null=True)),
                ('last_name', models.TextField(null=True)),
                ('email', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name': 'Import Record',
                'verbose_name_plural': 'Import Records',
            },
        ),
        migrations.CreateModel(
            name='ImportRecordStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[(b'success', b'Succeeded'), (b'failed', b'Failed')], max_length=50)),
                ('note', models.TextField(null=True)),
                ('import_record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_import.ImportRecord')),
            ],
            options={
                'verbose_name': 'Import Record Status',
                'verbose_name_plural': 'Import Record Statuses',
            },
            bases=(kennedy_common.utils.models.CacheMixinModel, models.Model),
        ),
        migrations.CreateModel(
            name='UserImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(null=True, storage=kennedy_common.utils.storages.HighValueStorage(), upload_to=b'user_imports/')),
                ('default', models.BooleanField(default=False, editable=False, verbose_name=b'Default API Import')),
            ],
            options={
                'verbose_name': 'User Import',
                'verbose_name_plural': 'User Imports',
            },
            bases=(kennedy_common.utils.models.CacheMixinModel, models.Model),
        ),
    ]