# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import oscar.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20150604_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattributevalue',
            name='value_multi_option',
            field=models.ManyToManyField(related_name='multi_valued_attribute_values', null=True, verbose_name='Value multi option', to='catalogue.AttributeOption', blank=True),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='code',
            field=models.SlugField(max_length=128, verbose_name='Code', validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z_][0-9a-zA-Z_]*$', message="Code can only contain the letters a-z, A-Z, digits, and underscores, and can't start with a digit."), oscar.core.validators.non_python_keyword]),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='option_group',
            field=models.ForeignKey(blank=True, to='catalogue.AttributeOptionGroup', help_text='Select an option group if using type "Option" or "Multi Option"', null=True, verbose_name='Option Group'),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='type',
            field=models.CharField(default=b'text', max_length=20, verbose_name='Type', choices=[(b'text', 'Text'), (b'integer', 'Integer'), (b'boolean', 'True / False'), (b'float', 'Float'), (b'richtext', 'Rich Text'), (b'date', 'Date'), (b'option', 'Option'), (b'multi_option', 'Multi Option'), (b'entity', 'Entity'), (b'file', 'File'), (b'image', 'Image')]),
        ),
    ]
