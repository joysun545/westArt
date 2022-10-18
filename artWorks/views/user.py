from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from artWorks import models
from artWorks.utils.bootstrap import BootstrapModelForm
from artWorks.utils.encrypt import md5
from artWorks.utils.pagination import Pagination




def user_list(request):
    """用户列表"""

    info_dict = request.session['info']

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
    queryset = models.UserInfo.objects.filter(**data_dict)

    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, 'user_list.html', context)


# 引用utils下bootstrap文件内的BootstrapModelForm格式插件
class UserInfoModelForm(BootstrapModelForm):
    # 在格式基础上添加一行表格
    confirm_password = forms.CharField(
        label="确认密码",
        # 添加widget=forms.PasswordInput密码不显示  render_value=True当密码不一致时第一次的密码不会被清空
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.UserInfo
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


def user_add(request):
    """"添加用户"""

    title = "注册新用户"

    if request.method == "GET":
        form = UserInfoModelForm()
        return render(request, 'currency.html', {
            "form": form,
            "title": title
        })

    form = UserInfoModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'currency.html', {
        "form": form,
        "title": title
    })


def user_edit(request, nid):
    """"""

    row_object = models.UserInfo.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html')

    title = "编辑用户"
    if request.method == "GET":
        # 加上instance=row_object属性和值，让编辑框里保留原始数据
        form = UserInfoModelForm(instance=row_object)
        context = {
            "title": title,
            "form": form
        }
        return render(request, 'currency.html', context)

    form = UserInfoModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    context = {
        "title": title,
        "form": form
    }
    return render(request, 'currency.html', context)


def user_delete(request, nid):
    """"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')


class UserResetModelForm(BootstrapModelForm):
    # 在格式基础上添加一行表格
    confirm_password = forms.CharField(
        label="确认密码",
        # 添加widget=forms.PasswordInput密码不显示  render_value=True当密码不一致时第一次的密码不会被清空
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.UserInfo
        fields = ["password", "confirm_password"]
        # 添加widget=forms.PasswordInput密码不显示  render_value=True当密码不一致时第一次的密码不会被清空
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 去数据库验证当前密码和新输入密码是否一致 （就是用现在密码区和库里面的密码比较，是不是存在
        exists = models.UserInfo.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
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


def user_reset(request, nid):
    """重置密码"""

    row_object = models.UserInfo.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html')

    title = "重置密码 - {}".format(row_object.username)
    if request.method == "GET":
        form = UserResetModelForm()
        context = {
            "title": title,
            "form": form
        }

        return render(request, 'currency.html', context)
    form = UserResetModelForm(data=request.POST, instance=row_object)
    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'currency.html', context)


