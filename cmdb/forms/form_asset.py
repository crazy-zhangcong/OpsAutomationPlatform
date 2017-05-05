#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:zhangcong
# Email:zc_92@sina.com


from django.forms import Form
from django.forms import widgets
from django.forms import MultipleChoiceField
from django.forms import fields

from cmdb import models


class AddAssetForm(Form):
    """新增资产Form表单"""

    device_type_id = fields.ChoiceField(
        choices=models.Asset.device_type_choices,
        widget=widgets.Select(
            attrs={}
        )

    )
    device_status_id = fields.ChoiceField(
        choices=models.Asset.device_status_choices,
        widget=widgets.Select

    )

    hostname = fields.CharField(
        error_messages={
            "required": "主机名不能为空",
        },
        widget=widgets.Input(
            attrs={"class": "form-control", "name": "hostname", "type": "text"})
    )

    cabinet_num = fields.CharField(
        required=False,
        widget=widgets.Input(
            attrs={"class": "form-control", "placeholder": "请输入机柜号,没有可为空", "name": "hostname", "type": "text"})
    )

    cabinet_order = fields.CharField(
        required=False,
        widget=widgets.Input(
            attrs={"class": "form-control", "placeholder": "请输入机柜中所在位置,没有可为空", "name": "hostname",
                   "type": "text"})
    )

    idc_id = fields.ChoiceField(
        error_messages={
            "required": "机房不能为空",
        },
        choices=[],
        widget=widgets.Select

    )

    business_unit_id = fields.ChoiceField(
        required=False,
        choices=[],
        widget=widgets.Select

    )

    tag = MultipleChoiceField(
        required=False,
        choices=models.Tag.objects.all().values_list('id', 'name'),
        widget=widgets.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super(AddAssetForm, self).__init__(*args, **kwargs)

        values = models.IDC.objects.all().values_list('id', 'name', 'floor')
        idc_values = [['', '---------']]
        for i in values:
            idc_values.append([i[0], "%s-%s" % (i[1], i[2])])
        self.fields['idc_id'].choices = idc_values

        values = models.BusinessUnit.objects.values_list('id', 'name')
        business_unit_values = [['', '---------']]
        for i in values:
            business_unit_values.append([i[0], i[1]])
        self.fields['business_unit_id'].choices = business_unit_values