# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cl_app.City')),
            ],
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cl_app.Category'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cl_app.City'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cl_app.Type'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=15),
        ),
        migrations.AddField(
            model_name='category',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cl_app.City'),
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cl_app.Type'),
        ),
    ]
