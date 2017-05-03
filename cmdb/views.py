from django.shortcuts import render

# Create your views here.


from index.views import is_login
from cmdb import models as cmdb_models


@is_login
def index(request):

    return render(request, "cmdb/index.html")


@is_login
def asset(request):
    if "type" in request.GET:
        from cmdb.views_func import asset
        asset_id = request.GET.get('id')
        if request.GET.get('type') == "select":     # 查看资产详情
            asset.SelectAsset(request, asset_id)

            return render(request, 'cmdb/asset_select.html')

        elif request.GET.get('type') == "edit":     # 编辑资产
            pass

        elif request.GET.get('type') == "create":   # 创建
            pass

        elif request.GET.get('type') == "delete":   # 删除资产
            pass

    cmdb_models_obj = cmdb_models.Asset.objects.all()

    return render(request, "cmdb/asset.html", locals())