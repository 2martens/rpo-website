# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpocore', '0005_auto_20160921_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supporter',
            name='university',
            field=models.CharField(choices=[('UHH', 'Universität Hamburg'), ('TUHH', 'Technische Universität Hamburg'), ('HAW', 'Hochschule für Angewandte Wissenschaften Hamburg'), ('HCU', 'HafenCity Universität Hamburg'), ('HFBK', 'Hochschule für bildende Künste Hamburg'), ('HfMT', 'Hochschule für Musik und Theater Hamburg'), ('HSU', 'Helmut-Schmidt-Universität Hamburg'), ('Other', 'Andere Universität oder Hochschule')], max_length=30, null=True, verbose_name='University'),
        ),
    ]