from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from artWorks import models
from artWorks.utils.bootstrap import BootstrapModelForm
from artWorks.utils.encrypt import md5
from artWorks.utils.pagination import Pagination


# 引用utils下bootstrap文件内的BootstrapModelForm格式插件
class UserInfoDetailsModelForm(BootstrapModelForm):
    """"""

    class Meta:
        model = models.UserInfo
        fields = ["username", "name","gender", "email", "mobile", "birthtime", "country", "city", "graduated", "artcategory",
                  "saysomethingmore"]


def userinfo_details(request,nid):
    """"添加用户"""

    obj = models.UserInfo.objects.filter(id=nid).first()

    return render(request, 'userinfo.html', {"obj":obj})


def userinfo_edit(request, nid):
    """"""

    row_object = models.UserInfo.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html')

    title = "编辑用户"
    if request.method == "GET":
        # 加上instance=row_object属性和值，让编辑框里保留原始数据
        form = UserInfoDetailsModelForm(instance=row_object)
        context = {
            "title": title,
            "form": form
        }
        return render(request, 'userinfo_edit.html', context)

    form = UserInfoDetailsModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/cover/')
    context = {
        "title": title,
        "form": form
    }
    return render(request, 'currency.html', context)


def userinfo_delete(request, nid):
    """"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')
