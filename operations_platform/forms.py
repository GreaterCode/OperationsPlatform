# _*_ coding: utf-8 _*_

from django.forms import ModelForm
from .models import Node, Line, Device

# 定义Node的Form
class NodeForm(ModelForm):
    # 自定义ModeForm的内容
    class Meta:
        model = Node
        exclude = ['node_signer']

class LineForm(ModelForm):
    class Meta:
        model = Line
        exclude = ['line_signer']

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = ['device_signer']

