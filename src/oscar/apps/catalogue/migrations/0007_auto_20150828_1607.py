# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20150828_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattributevalue',
            name='value_multi_option',
            field=models.ManyToManyField(related_name='multi_valued_attribute_values', verbose_name='Value multi option', to='catalogue.AttributeOption', blank=True),
        ),
    ]
