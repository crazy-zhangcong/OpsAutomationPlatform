#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:zhangcong
# Email:zc_92@sina.com

from cmdb import models
from django.shortcuts import render

def CreateAsset():
    pass


def DeleteAsset(asset_id):
    pass


def EditAsset(asset_id):
    pass


def SelectAsset(request, asset_id):  # 查看资产

    result_data = {}

    # 基本信息
    get_basic_data(request, asset_id)

    print('xxx')


def get_status_name(obj):
    """获取状态名称"""
    status_choices = obj.device_status_choices
    for i in status_choices:
        if i[0] == obj.device_status_id:
            status = i[1]
            return status


def get_basic_data(request, asset_id):
    basic_data = {}
    obj = models.Asset.objects.get(id=asset_id)

    # 显示服务器信息
    if obj.device_type_id in [1, 2]:
        hostname = obj.server.hostname      # 主机名
        manage_ip = obj.server.manage_ip    # 管理ip
        sn = obj.server.sn                  # 序列号/sn号
        status = get_status_name(obj)       # 状态名称
        latest_date = obj.latest_date       # 更新时间
        idc = obj.idc.name                  # 机房
        floor = obj.idc.floor               # 楼层
        cabinet_num = obj.cabinet_num       # 机柜号
        cabinet_order = obj.cabinet_order   # 机柜中位置
        business_unit = obj.business_unit.name  # 业务线






    # 显示网络设备信息
    else:
        pass



