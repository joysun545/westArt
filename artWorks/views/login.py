from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.six import BytesIO

from artWorks import models
from artWorks.utils.bootstrap import BootstrapModelForm, BootstrapForm
from artWorks.utils.code import check_code
from artWorks.utils.encrypt import md5
from artWorks.utils.pagination import Pagination


class LoginForm(BootstrapForm):
    username = forms.CharField(
        label="昵称",
        widget=forms.TextInput
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True)
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)
        return md5_pwd


def login(request):
    """用户登陆"""

    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # 验证码校验 用pop方法获取，可以将数据从列表中扣除，便于后续username,password 的校验
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', '')
        if code.upper() != user_input_code.upper():
            form.add_error('code', '验证码错误')
            return render(request, 'login.html', {'form': form})
        # 去数据库校验用户名和密码是否正确，获取用户对象，None
        admin_object = models.UserInfo.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        # session可以保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/cover/')
    return render(request, 'login.html', {"form": form})


def image_code(request):
    """生成图片验证码"""

    # 调用pillow函数生成图片
    img, code_str = check_code()

    # 把code_str写入自己的session中，以便后续获取验证码进行校验
    request.session['image_code'] = code_str
    # 给session设置一个60秒超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')

    return HttpResponse(stream.getvalue())


def logout(request):
    """注销"""

    request.session.clear()
    return redirect('/cover/')
