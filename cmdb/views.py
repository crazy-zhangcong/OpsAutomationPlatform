from django.shortcuts import render

# Create your views here.


from index.views import is_login
from cmdb import models as cmdb_models


@is_login
def index(request):

    return render(request, "cmdb/index.html")


@is_login
def asset(request):

    cmdb_models_obj = cmdb_models.Asset.objects.all()

    return render(request, "cmdb/asset.html", locals())