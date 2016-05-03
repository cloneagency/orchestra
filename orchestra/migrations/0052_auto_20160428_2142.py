# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orchestra', '0051_delete_timeentries_no_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeentry',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_entries', to='orchestra.Worker'),
        ),
    ]