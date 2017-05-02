#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:zhangcong
# Email:zc_92@sina.com


from django import template

register = template.Library()   # 这一句必须这样写


@register.simple_tag
def display_asset_type_name(line_obj):
    """
    根据资产类型ID 从 choices 中获取资产类型的名称
    :param line_obj:  表中每一行数据的对象
    :return:
    """

    for i in line_obj.device_type_choices:
        if line_obj.device_type_id == i[0]:
            asset_type_name = i[1]
            return asset_type_name


@register.simple_tag
def display_asset_status_name(line_obj):
    """
    根据资产状态ID 从 choices 中获取资产类型的名称
    :param line_obj: 表中每一行数据的对象
    :return:
    """

    for i in line_obj.device_status_choices:
        if line_obj.device_status_id == i[0]:
            asset_status_name = i[1]
            return asset_status_name


@register.simple_tag
def display_asset_tags_name(line_obj):
    tags_obj = line_obj.tag.all()

    tag_names = None
    for obj in tags_obj:
        if tag_names:
            tag_names += ",%s" % obj.name
        else:
            tag_names = obj.name

    return tag_names