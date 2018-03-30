# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def assign_primary_domain(apps, schema_editor):
    """Assign a default primary domain for each org"""
    Organization = apps.get_model('branding', 'Organization')

    for organization in Organization.objects.all():
        organization.primary_domain = organization.domain_set.first()
        organization.save()


class Migration(migrations.Migration):

    dependencies = [
        ('branding', '0002_organization_elections'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='primary_domain',
            field=models.ForeignKey(default=1, help_text=b'Domain to attach all links to', on_delete=django.db.models.deletion.CASCADE, related_name='primary_domain', to='branding.Domain', verbose_name=b'Primary Domain'),
            preserve_default=False,
        ),
        migrations.RunPython(assign_primary_domain, lambda x, y: None)
    ]
