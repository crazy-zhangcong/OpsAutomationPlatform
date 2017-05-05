#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:zhangcong
# Email:zc_92@sina.com

from cmdb import models
from index import models as index_models

from cmdb.forms import form_asset


def CreateAsset(obj):

    hostname = obj.cleaned_data.pop('hostname')
    Server_obj = models.Server.objects.filter(hostname=hostname)

    if Server_obj:  # 判断主机名是否存在
        # 主机名已经存在
        obj.errors['hostname'] = ["主机名已存在"]
    else:
        tag_list = obj.cleaned_data.pop('tag')

        Asset_obj = models.Asset.objects.create(**obj.cleaned_data)

        models.Server.objects.create(hostname=hostname, asset_id=Asset_obj.id)

        if tag_list:
            tag_obj = models.Tag.objects.filter(id__in=tag_list)
            Asset_obj.tag.add(*tag_obj)
    return obj

def DeleteAsset(asset_id):
    pass


def EditAsset(asset_id):
    pass


def SelectAsset(asset_id):  # 查看资产,获取资产的详细信息

    obj = models.Asset.objects.get(id=asset_id)

    # 服务器信息
    if obj.device_type_id in [1, 2]:

        result_data = {
            'type': 'server',       # 用于区分是网络设备还是服务器设备,根据该值选择不同的模板进行渲染
            'basic_data': get_basic_data(obj, asset_id),      # 基本信息
            'hardware_data': get_hardware_data(asset_id),     # 硬件信息
            'log_data': get_log_data(asset_id)                # 资产变更日志
        }

    # 网络设备信息
    else:
        result_data = {
            'type': 'network',      # 用于区分是网络设备还是服务器设备,根据该值选择不同的模板进行渲染
        }
    return result_data


# ######### 获取资产基本信息 ##########
def get_status_name(obj):
    """获取状态名称"""
    status_choices = obj.device_status_choices
    for i in status_choices:
        if i[0] == obj.device_status_id:
            status = i[1]
            return status


def get_contact_information(obj):
    """获取管理该资产的人员信息"""

    #### 业务联系人 ####
    contact_group_id = obj.business_unit.contact  # 业务负责组id
    contact_data = []
    contact_obj = index_models.UserGroup.objects.get(id=contact_group_id)

    c_obj = contact_obj.users.all()     # 这里是多对多,所以需要查一次
    for i in c_obj:

        contact_info = {
            'name': i.name,
            'email': i.email,
            'mobile': i.mobile,
            'phone': i.phone,
        }
        contact_data.append(contact_info)

    #### 运维联系人 ####
    manager_group_id = obj.business_unit.manager  # 运维负责组id
    manager_data = []
    manager_obj = index_models.UserGroup.objects.get(id=manager_group_id)
    m_obj = manager_obj.users.all()  # 这里是多对多,所以需要查一次
    for i in m_obj:
        manager_info = {
            'name': i.name,
            'email': i.email,
            'mobile': i.mobile,
            'phone': i.phone,
        }
        manager_data.append(manager_info)
    return contact_data, manager_data


def get_basic_data(obj, asset_id):
    """获取资产基本信息"""

    # 业务线信息和业务线负责人信息
    business_data = {}
    if obj.business_unit:
        business_unit = obj.business_unit.name  # 业务线
        contact_data, manager_data = get_contact_information(obj)
        business_data = {
            'business_unit': business_unit,
            'contact_data': contact_data,
            'manager_data': manager_data,
        }

    basic_data = {
        'hostname': obj.server.hostname,        # 主机名
        'manage_ip': obj.server.manage_ip,      # 管理ip
        'sn': obj.server.sn,                    # 序列号/sn号
        'status': get_status_name(obj),         # 状态名称
        'latest_date': obj.latest_date,         # 更新时间
        'idc': obj.idc.name,                    # 机房
        'floor': obj.idc.floor,                 # 楼层
        'cabinet_num': obj.cabinet_num,         # 机柜号
        'cabinet_order': obj.cabinet_order,     # 机柜中位置
        'business_data': business_data,
    }

    return basic_data

# ######### 获取资产基本信息 ##########


# ######### 获取资产硬件信息 ##########
def get_base_data(asset_id):
    """硬件基础信息"""
    obj = models.Server.objects.get(asset_id=asset_id)
    base_data = {
        'os_platform': obj.os_platform,
        'os_version': obj.os_version,
        'sn': obj.sn,
        'model': obj.model,
        'manufacturer': obj.manufacturer,
        'cpu_count': obj.cpu_count,
        'cpu_physical_count': obj.cpu_physical_count,
        'cpu_model': obj.cpu_model,
    }

    return base_data


def get_nic_data(asset_id):
    """获取网卡信息"""
    obj = models.NIC.objects.filter(server_obj_id=asset_id)
    nic_data = []
    for i in obj:
        data = {
            'name': i.name,
            'hwaddr': i.hwaddr,
            'ipaddrs': i.ipaddrs,
            'netmask': i.netmask,
            'up': i.up,
        }
        nic_data.append(data)

    return nic_data


def get_disk_data(asset_id):
    """获取硬盘信息"""
    obj = models.Disk.objects.filter(server_obj_id=asset_id)
    disk_data = []
    for i in obj:
        data = {
            'slot': i.slot,
            'capacity': i.capacity,
            'pd_type': i.pd_type,
            'model': i.model,
        }
        disk_data.append(data)

    return disk_data


def get_memory_data(asset_id):
    """获取内存信息"""
    obj = models.Memory.objects.filter(server_obj_id=asset_id)
    memory_data = []
    for i in obj:
        data = {
            'slot': i.slot,
            'capacity': i.capacity,
            'speed': i.speed,
            'model': i.model,
        }
        memory_data.append(data)

    return memory_data


def get_hardware_data(asset_id):
    """获取资产硬件信息"""

    hardware_data = {
        'base_data': get_base_data(asset_id),     # 基础信息
        'nic_data': get_nic_data(asset_id),       # 网卡信息
        'disk_data': get_disk_data(asset_id),     # 硬盘信息
        'memory_data': get_memory_data(asset_id),     # 内存信息
    }

    return hardware_data

# ######### 获取资产硬件信息 ##########


# ######### 获取资产日志信息 ##########
def get_log_data(asset_id):
    obj = models.AssetRecord.objects.filter(asset_obj_id=asset_id)
    log_data = []
    for i in obj:
        if i.creator:
            user_obj = index_models.UserProfile.objects.get(id=i.creator)
            creator = user_obj.name
        else:
            creator = "资产搜集"
        data = {
            'create_at': i.create_at,
            'content': i.content,
            'creator': creator,
        }
        log_data.append(data)

    return log_data

# ######### 获取资产日志信息 ##########