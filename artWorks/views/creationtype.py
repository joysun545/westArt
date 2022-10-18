from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from artWorks import models
from artWorks.utils.bootstrap import BootstrapModelForm
from artWorks.utils.encrypt import md5
from artWorks.utils.pagination import Pagination


def creationtype_list(request):
    """"""

    # info_dict = request.session['info']

    # 检查用户是否已经登录，已登录，继续往下走，未登录，跳转回登录页面
    # 用户发来请求，获取cookie随机字符串，拿着随机字符串看看session中有没有
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')

    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["creationtype__contains"] = search_data
    # 根据搜索条件到数据库获取filter(**search_data)
    queryset = models.CreationTypeInfo.objects.filter(**data_dict)

    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, 'creationtype_list.html', context)


# 引用utils下bootstrap文件内的BootstrapModelForm格式插件
class CreationTypeInfoModelForm(BootstrapModelForm):

    class Meta:
        model = models.CreationTypeInfo
        fields = "__all__"


def creationtype_add(request):
    """"添加创作类型"""

    title = "添加创作类型"

    if request.method == "GET":
        form = CreationTypeInfoModelForm()
        return render(request, 'currency.html', {
            "form": form,
            "title": title
        })

    form = CreationTypeInfoModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/creationtype/list/')
    return render(request, 'currency.html', {
        "form": form,
        "title": title
    })


def creationtype_edit(request, nid):
    """"""

    row_object = models.CreationTypeInfo.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html')

    title = "编辑艺术门类"
    if request.method == "GET":
        # 加上instance=row_object属性和值，让编辑框里保留原始数据
        form = CreationTypeInfoModelForm(instance=row_object)
        context = {
            "title": title,
            "form": form
        }
        return render(request, 'currency.html', context)

    form = CreationTypeInfoModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/creationtype/list')
    context = {
        "title": title,
        "form": form
    }
    return render(request, 'currency.html', context)


def creationtype_delete(request, nid):
    """"""
    models.CreationTypeInfo.objects.filter(id=nid).delete()
    return redirect('/creationtype/list/')
