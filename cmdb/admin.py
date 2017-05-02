from django.contrib import admin

# Register your models here.


from cmdb import models


admin.site.register(models.Asset)
admin.site.register(models.AssetRecord)
admin.site.register(models.BusinessUnit)
admin.site.register(models.Disk)
admin.site.register(models.ErrorLog)
admin.site.register(models.IDC)
admin.site.register(models.Memory)
admin.site.register(models.NetworkDevice)
admin.site.register(models.NIC)
admin.site.register(models.Server)
admin.site.register(models.Tag)