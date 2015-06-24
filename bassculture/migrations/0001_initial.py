# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.IntegerField(db_index=True, unique=True)),
                ('surname', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['surname'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField(db_index=True, unique=True)),
                ('full_title', models.CharField(max_length=255)),
                ('short_title', models.CharField(max_length=255)),
                ('edition', models.CharField(max_length=16)),
                ('date', models.CharField(max_length=16)),
                ('link', models.URLField(null=True, blank=True)),
                ('link_label', models.TextField(null=True, blank=True)),
                ('rism', models.CharField(max_length=16)),
                ('gore', models.CharField(max_length=16)),
                ('pagination', models.CharField(max_length=8)),
                ('orientation', models.CharField(max_length=16, null=True, choices=[('l', 'landscape'), ('p', 'portrait')], blank=True)),
                ('dimensions', models.CharField(max_length=8)),
                ('library', models.CharField(max_length=40, null=True, blank=True)),
                ('shelfmark', models.CharField(max_length=16)),
                ('item_notes', models.TextField(null=True, blank=True)),
                ('additional_items', models.TextField(null=True, blank=True)),
                ('authors', models.ManyToManyField(related_name='items', to='bassculture.Author', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printer_id', models.IntegerField(db_index=True, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Printer')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_id', models.IntegerField(db_index=True, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_id', models.IntegerField(db_index=True, unique=True)),
                ('name', models.CharField(max_length=255, db_index=True, verbose_name='Seller')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField(db_index=True, unique=True)),
                ('title', models.CharField(max_length=255, db_index=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('source_notes', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='printer',
            field=models.ForeignKey(related_name='items', to='bassculture.Printer', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='publisher',
            field=models.ForeignKey(related_name='items', to='bassculture.Publisher', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(related_name='items', to='bassculture.Seller', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='source',
            field=models.ForeignKey(to='bassculture.Source'),
        ),
    ]
