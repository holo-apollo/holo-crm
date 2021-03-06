# Generated by Django 2.2.4 on 2019-08-12 18:13

import apps.common.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=apps.common.fields.PhoneField(blank=True, default='', error_messages={'unique': 'That phone number is already taken.'}, max_length=13, unique=True, verbose_name='Phone'),
        ),
    ]
