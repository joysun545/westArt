from datetime import datetime
from random import random

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from artWorks import models
from artWorks.utils.bootstrap import BootstrapModelForm
from artWorks.utils.pagination import Pagination


class CompleteWorkSecondModelForm(BootstrapModelForm):
    class Meta:
        model = models.CompleteWorksInfo
        # fields = "__all__"
        exclude = ["sharer"]


def completeworks02_list(request):
    """工单"""
    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["artistname__contains"] = search_data
    # 根据搜索条件到数据库获取filter(**search_data)
    queryset = models.CompleteWorksInfo.objects.filter(**data_dict).order_by('-id')

    # queryset = models.CompleteWorksInfo.objects.all().order_by('-id')
    page_object = Pagination(request, queryset,page_size=5)
    form = CompleteWorkSecondModelForm()
    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "form": form,
    }

    return render(request, 'completeworks02.html', context)


@csrf_exempt
def completeworks02_add(request):
    """"新建"""
    form = CompleteWorkSecondModelForm(data=request.POST)
    if form.is_valid():
        # 固定设置分享者ID（所在userinfo列表中的ID）
        form.instance.sharer_id = request.session["info"]["id"]
        form.save()
        return JsonResponse({
            "status": True
        })
    return JsonResponse({
        "status": False,
        "error": form.errors
    })


def completeworks02_delete(request):
    """删除订单"""
    uid = request.GET.get('uid')
    exists = models.CompleteWorksInfo.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "数据不存在"})
    models.CompleteWorksInfo.objects.filter(id=uid).delete()
    print(uid)
    return JsonResponse({"status": True, "error": "数据不存在"})


def completeworks02_detail(request):
    """根据ID获取订单详情订单"""
    """方法一"""
    # uid = request.GET.get("uid")
    # row_object = models.Order.objects.filter(id=uid).first()
    # if not row_object:
    #     return JsonResponse({"status": False, "error": "数据不存在"})
    # # 从数据库中获取到了一个对象row_objec
    # result = {
    #     "status":True,
    #     "data" : {
    #     "title": row_object.title,
    #     "price": row_object.price,
    #     "status": row_object.status,
    #     }
    # }
    # return JsonResponse({"status":True,"data":result})
    """方法二"""
    uid = request.GET.get("uid")
    row_dict = models.CompleteWorksInfo.objects.filter(id=uid).values("name","artistname","artcreationtype","creationtime","collectionmuseum","uploadtime").first()
    if not row_dict:
        return JsonResponse({"status": False, "error": "数据不存在"})
    # 从数据库中获取到了一个字典row_dict
    result = {
        "status": True,
        "data": row_dict
    }
    return JsonResponse({"status": True, "data": row_dict})


@csrf_exempt
def completeworks02_edit(request):
    """编辑订单"""
    uid = request.GET.get("uid")
    row_object = models.CompleteWorksInfo.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "summary": "数据不存在。"})
    form = CompleteWorkSecondModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})


