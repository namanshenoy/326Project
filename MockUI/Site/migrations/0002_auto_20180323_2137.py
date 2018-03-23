# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-23 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historyentry',
            options={'verbose_name': 'History Entry', 'verbose_name_plural': 'History Entries'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': 'User Information', 'verbose_name_plural': 'User Information'},
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.RemoveField(
            model_name='store',
            name='coupons',
        ),
        migrations.RemoveField(
            model_name='store',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Site.Product'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='date_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_type',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='historyentry',
            name='date_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historyentry',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Site.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='product',
            name='source',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='views',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='store',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='store',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site.Cart'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site.HistoryEntry'),
        ),
    ]