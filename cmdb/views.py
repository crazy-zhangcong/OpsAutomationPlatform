from django.shortcuts import render, redirect

# Create your views here.


from index.views import is_login
from cmdb import models as cmdb_models

from cmdb.forms import form_asset


@is_login
def index(request):

    return render(request, "cmdb/index.html")


@is_login
def asset(request):
    if "type" in request.GET:
        from cmdb.views_func import asset
        asset_id = request.GET.get('id')
        if request.GET.get('type') == "select":     # 查看资产详情
            result_data = asset.SelectAsset(asset_id)

            return render(request, 'cmdb/asset_select.html', locals())

        elif request.GET.get('type') == "edit":     # 编辑资产
            pass

        elif request.GET.get('type') == "create":   # 创建
            if request.method == "GET":
                obj = form_asset.AddAssetForm()
                return render(request, 'cmdb/asset_create.html', {'obj': obj})
            elif request.method == "POST":
                obj = form_asset.AddAssetForm(request.POST)

                if obj.is_valid():
                    obj = asset.CreateAsset(obj)
                    print(obj.errors)
                    if not obj.errors:
                        return redirect('/cmdb/asset.html')

                return render(request, 'cmdb/asset_create.html', {'obj': obj})

        elif request.GET.get('type') == "delete":   # 删除资产
            pass

    cmdb_models_obj = cmdb_models.Asset.objects.all()

    return render(request, "cmdb/asset.html", locals())