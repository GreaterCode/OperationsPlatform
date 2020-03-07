from django.shortcuts import render
from .models import Node

# Create your views here.
def lists(request):
    # 从node节点中获取所有数据
    data = Node.objects.all()

    # 建立context字典，将值传递到页面
    context = {
        'data': data,
    }

    return render(request, 'lists.html', context)