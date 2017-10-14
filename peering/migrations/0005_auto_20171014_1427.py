# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peering', '0004_auto_20171004_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('hostname', models.CharField(max_length=256)),
                ('platform', models.CharField(choices=[('junos', 'Juniper JUNOS'), ('iosxr', 'Cisco IOS-XR'), (None, 'Other')], help_text='The router platform, used to interact with it', max_length=50)),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='internetexchange',
            name='router',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='peering.Router'),
        ),
    ]
