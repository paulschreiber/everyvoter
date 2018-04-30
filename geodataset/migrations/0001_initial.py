# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-30 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_smalluuid.models
import everyvoter_common.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branding', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', django_smalluuid.models.SmallUUIDField(db_index=True, default=django_smalluuid.models.UUIDDefault(), editable=False, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('value', models.TextField(verbose_name=b'Value')),
            ],
            options={
                'verbose_name': 'Field',
                'verbose_name_plural': 'Fields',
            },
            bases=(everyvoter_common.utils.models.CacheMixinModel, models.Model),
        ),
        migrations.CreateModel(
            name='GeoDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', django_smalluuid.models.SmallUUIDField(db_index=True, default=django_smalluuid.models.UUIDDefault(), editable=False, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('organization', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='branding.Organization')),
            ],
            options={
                'verbose_name': 'GeoDataset',
                'verbose_name_plural': 'GeoDatasets',
            },
            bases=(everyvoter_common.utils.models.CacheMixinModel, models.Model),
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', django_smalluuid.models.SmallUUIDField(db_index=True, default=django_smalluuid.models.UUIDDefault(), editable=False, unique=True)),
                ('geodataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geodataset.GeoDataset')),
            ],
            options={
                'verbose_name': 'Geo Dataset Row',
                'verbose_name_plural': 'Geo Dataset Rows',
            },
            bases=(everyvoter_common.utils.models.CacheMixinModel, models.Model),
        ),
        migrations.AddField(
            model_name='field',
            name='row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geodataset.Row'),
        ),
    ]
