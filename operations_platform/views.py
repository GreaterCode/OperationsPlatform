#
from django.shortcuts import render, redirect
from .models import Node
from .forms import NodeForm, LineForm, DeviceForm

# Create your views here.
def lists(request):
    # 从node节点中获取所有数据
    data = Node.objects.all()

    # 建立context字典，将值传递到页面
    context = {
        'data': data,
    }

    return render(request, 'lists.html', context)


def add(request):
    # 获取NodeForm表单数据
    form = NodeForm(request.POST or None)

    # 判断form是否有效
    if form.is_valid():
        instance = form.save(commit=False)
        instance.node_signer = request.user
        instance.save()

        return redirect('/lists/')

    # 创建context来集中处理需要传递到页面的数据
    context = {
        'form': form,
    }

    # 如果没有有效提交，则跳转值原来页面
    return render(request, 'add.html', context)



