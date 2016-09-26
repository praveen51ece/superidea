# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravellerDetails',
            fields=[
                ('tvl_code', models.AutoField(help_text=b'0', serialize=False, primary_key=True)),
                ('tvl_name', models.CharField(help_text=b'1', max_length=30, verbose_name=b'Name')),
                ('tvl_emailid', models.CharField(help_text=b'1', max_length=50, verbose_name=b'Email Id')),
                ('tvl_cc_list', models.CharField(max_length=300, null=True, blank=True)),
                ('tvl_password', models.CharField(help_text=b'0', max_length=20, null=True, blank=True)),
                ('tvl_mobile', models.CharField(help_text=b'1', max_length=25, verbose_name=b'Mobile')),
                ('tvl_phone', models.CharField(help_text=b'1', max_length=25, verbose_name=b'Phone')),
                ('tvl_company', models.CharField(help_text=b'1', max_length=50, verbose_name=b'Company you work', blank=True)),
                ('tvl_last_login', models.DateTimeField(help_text=b'0')),
                ('tvl_isused', models.IntegerField(default=0, help_text=b'0')),
                ('tvl_createdon', models.DateTimeField(help_text=b'0', auto_now_add=True)),
                ('tvl_lastmodon', models.DateTimeField(help_text=b'0', auto_now=True)),
                ('tvl_display', models.BooleanField(default=True)),
                ('tvl_isb2b', models.BooleanField(default=False)),
                ('tvl_b2bagentname', models.CharField(max_length=30, null=True, blank=True)),
                ('tvl_b2bagentcity', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
    ]
