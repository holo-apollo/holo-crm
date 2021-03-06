# Generated by Django 2.2.4 on 2019-08-11 19:40

import apps.common.fields
import django.contrib.postgres.fields.citext
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'That username is already taken.'}, max_length=30, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(blank=True, default='', max_length=30, verbose_name='First name')),
                ('first_name_en', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='First name')),
                ('first_name_ru', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='First name')),
                ('first_name_uk', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, default='', max_length=30, verbose_name='Last name')),
                ('last_name_en', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Last name')),
                ('last_name_ru', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Last name')),
                ('last_name_uk', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Last name')),
                ('email', django.contrib.postgres.fields.citext.CIEmailField(error_messages={'unique': 'That email address is already taken.'}, max_length=254, unique=True, verbose_name='Email')),
                ('phone', apps.common.fields.PhoneField(blank=True, error_messages={'unique': 'That phone number is already taken.'}, max_length=13, null=True, unique=True, verbose_name='Phone')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('avatar', models.URLField(blank=True, null=True, verbose_name='Avatar')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
