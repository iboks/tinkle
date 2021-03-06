# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-31 11:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import internationalflavor.vat_number.models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('silson', '0002_auto_20160823_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalAffiliation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True, null=True)),
                ('comments', models.TextField(blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('associate', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='silson.Customer')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='silson.User')),
            ],
            options={
                'verbose_name': 'historical affiliation',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCustomer',
            fields=[
                ('account_ID', models.CharField(db_index=True, max_length=16)),
                ('full_Name', models.CharField(blank=True, max_length=96)),
                ('acronym', models.CharField(blank=True, max_length=32)),
                ('website', models.URLField(blank=True)),
                ('address', models.CharField(max_length=100)),
                ('telephone', models.CharField(blank=True, max_length=16)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('us_state', localflavor.us.models.USStateField(blank=True)),
                ('VAT', internationalflavor.vat_number.models.VATNumberField(blank=True)),
                ('date_added', models.DateField()),
                ('customer_type', models.CharField(choices=[('Gov', 'Government'), ('Edu', 'Education'), ('Co', 'Corporation'), ('Ind', 'Individual'), ('Pri', 'Private')], max_length=3)),
                ('status', models.CharField(choices=[('V', 'Valid'), ('I', 'Invalid')], max_length=8)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('added_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='silson.Staff')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical customer',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
    ]
