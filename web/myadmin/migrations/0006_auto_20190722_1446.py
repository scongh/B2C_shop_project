# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-22 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_auto_20190722_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'permissions': (('show_Goods', '查看商品列表权限'), ('create_Goods', '添加商品权限'), ('edit_Goods', '修改商品信息权限'), ('delete_Goods', '删除商品权限'))},
        ),
    ]