from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from artWorks import models
from artWorks.utils.bootstrap import BootstrapModelForm
from artWorks.utils.encrypt import md5
from artWorks.utils.pagination import Pagination


def admin_list(request):
    """管理员列表"""

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
        data_dict["username__contains"] = search_data
    # 根据搜索条件到数据库获取filter(**search_data)
    queryset = models.AdminInfo.objects.filter(**data_dict)

    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, 'admin_list.html', context)


# 引用utils下bootstrap文件内的BootstrapModelForm格式插件
class AdminInfoModelForm(BootstrapModelForm):
    # 在格式基础上添加一行表格
    confirm_password = forms.CharField(
        label="确认密码",
        # 添加widget=forms.PasswordInput密码不显示  render_value=True当密码不一致时第一次的密码不会被清空
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.AdminInfo
        fields = ["username", "password", "confirm_password"]
        # 添加以下格式，密码不显示 render_value=True当密码不一致时第一次的密码不会被清空
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")

        return confirm


def admin_add(request):
    """"添加管理员"""

    title = "添加管理员"

    if request.method == "GET":
        form = AdminInfoModelForm()
        return render(request, 'currency.html', {
            "form": form,
            "title": title
        })

    form = AdminInfoModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'currency.html', {
        "form": form,
        "title": title
    })


def admin_edit(request, nid):
    """"""

    row_object = models.AdminInfo.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html')

    title = "编辑管理员"
    if request.method == "GET":
        # 加上instance=row_object属性和值，让编辑框里保留原始数据
        form = AdminInfoModelForm(instance=row_object)
        context = {
            "title": title,
            "form": form
        }
        return render(request, 'currency.html', context)

    form = AdminInfoModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    context = {
        "title": title,
        "form": form
    }
    return render(request, 'currency.html', context)


def admin_delete(request, nid):
    """"""
    models.AdminInfo.objects.filter(id=nid).delete()
    return redirect('/admin/list/')


class AdminInfoResetModelForm(BootstrapModelForm):
    # 在格式基础上添加一行表格
    confirm_password = forms.CharField(
        label="确认密码",
        # 添加widget=forms.PasswordInput密码不显示  render_value=True当密码不一致时第一次的密码不会被清空
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.AdminInfo
        fields = ["password", "confirm_password"]
        # 添加widget=forms.PasswordInput密码不显示  render_value=True当密码不一致时第一次的密码不会被清空
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 去数据库验证当前密码和新输入密码是否一致 （就是用现在密码区和库里面的密码比较，是不是存在
        exists = models.AdminInfo.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        # 如果存在，报错
        if exists:
            raise ValidationError("密码不能与之前的相同")

        return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")

        return confirm


def admin_reset(request, nid):
    """重置密码"""

    row_object = models.AdminInfo.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html')

    title = "重置密码 - {}".format(row_object.username)
    if request.method == "GET":
        form = AdminInfoResetModelForm()
        context = {
            "title": title,
            "form": form
        }

        return render(request, 'currency.html', context)
    form = AdminInfoResetModelForm(data=request.POST, instance=row_object)
    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'currency.html', context)

