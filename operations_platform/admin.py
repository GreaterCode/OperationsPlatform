from django.contrib import admin
from .models import Node, Line, Device

# Register your models here.


#
class NodeAdmin(admin.ModelAdmin):
    # 添加保存后，需要添显示的字段
    list_display = ('node_name', 'node_address', 'node_signer')
    exclude = ['node_signer']

    # 将登录用户设置为登记人
    def save_model(self, request, obj, form, change):
        obj.node_signer = str(request.user)
        obj.save()


class LineAdmin(admin.ModelAdmin):
    # 在编辑、新增页面排除line_signer选项
    exclude = ('line_signer', )

    #对保存函数进行更改，将登陆用户设置为登记人
    def save_model(self, request, obj, form, change):
        obj.line_signer = str(request.user)
        obj.save()

class DeviceAdmin(admin.ModelAdmin):
    # 在编辑、新增页面上排除device_signer的选项
    exclude = ('device_signer', )

    # 对保存函数进行更改，将登录人设置为登记人
    def save_model(self, request, obj, form, change):
        obj.device_signer = str(request.user)
        obj.save()


admin.site.register(Node, NodeAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Device, DeviceAdmin)

