# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-22 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0008_order_orderinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cates',
            options={'permissions': (('show_Cates', '查看商品分类列表权限'), ('create_Cates', '添加商品分类权限'), ('edit_Cates', '修改商品分类信息权限'), ('remove_Cates', '删除商品分类权限'))},
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'permissions': (('show_Goods', '查看商品列表权限'), ('create_Goods', '添加商品权限'), ('edit_Goods', '修改商品信息权限'), ('remove_Goods', '删除商品权限'))},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': (('show_Order', '查看订单列表权限'), ('create_Order', '添加订单权限'), ('edit_Order', '修改订单信息权限'), ('remove_Order', '删除订单权限'))},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'permissions': (('show_Users', '查看会员列表权限'), ('create_Users', '添加会员权限'), ('edit_Users', '修改会员信息权限'), ('remove_Users', '删除会员权限'))},
        ),
    ]