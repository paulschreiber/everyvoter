# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-31 15:54
from __future__ import unicode_literals

from django.db import migrations, models


demonyms = (
    ('AL', 'Alabamians'),
    ('AK', 'Alaskans'),
    ('AZ', 'Arizonans'),
    ('AR', 'Arkansans'),
    ('CA', 'Californians'),
    ('CO', 'Coloradans'),
    ('CT', 'Connecticuters'),
    ('DE', 'Delawareans'),
    ('FL', 'Floridians'),
    ('GA', 'Georgians'),
    ('HI', 'Hawaiians'),
    ('ID', 'Idahoans'),
    ('IL', 'Illinoisans'),
    ('IN', 'Hoosiers'),
    ('IA', 'Iowans'),
    ('KS', 'Kansans'),
    ('KY', 'Kentuckians'),
    ('LA', 'Louisianians'),
    ('ME', 'Mainers'),
    ('MD', 'Marylanders'),
    ('MA', 'Massachusettsans'),
    ('MI', 'Michiganders'),
    ('MN', 'Minnesotans'),
    ('MS', 'Mississippians'),
    ('MO', 'Missourians'),
    ('MT', 'Montanans'),
    ('NE', 'Nebraskans'),
    ('NV', 'Nevadans'),
    ('NH', 'New Hampshirites'),
    ('NJ', 'New Jerseyans'),
    ('NM', 'New Mexicans'),
    ('NY', 'New Yorkers'),
    ('NC', 'North Carolinians'),
    ('ND', 'North Dakotans'),
    ('OH', 'Ohioans'),
    ('OK', 'Oklahomans'),
    ('OR', 'Oregonians'),
    ('PA', 'Pennsylvanians'),
    ('RI', 'Rhode Islanders'),
    ('SC', 'South Carolinians'),
    ('SD', 'South Dakotans'),
    ('TN', 'Tennesseans'),
    ('TX', 'Texans'),
    ('UT', 'Utahns'),
    ('VT', 'Vermonters'),
    ('VA', 'Virginians'),
    ('WA', 'Washingtonians'),
    ('WV', 'West Virginians'),
    ('WI', 'Wisconsinites'),
    ('WY', 'Wyomingites'),
    ('DC', 'Washingtonians')
)

def load_demonyms(apps, schema_editor):
    """Load state demonyms"""
    State = apps.get_model('election', 'State')

    for denonym in demonyms:
        State.objects.filter(code=denonym[0]).update(demonym=denonym[1])


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0003_load_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='demonym',
            field=models.CharField(default='', max_length=50, verbose_name=b'Demonym'),
            preserve_default=False,
        ),
        migrations.RunPython(load_demonyms, lambda x, y: None),
    ]
