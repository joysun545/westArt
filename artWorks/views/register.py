
from django.shortcuts import render, redirect

from artWorks.views.user import UserInfoModelForm


def user_register(request):
    """"新用户注册"""

    title = "新用户注册"

    if request.method == "GET":
        form = UserInfoModelForm()
        return render(request, 'register.html', {
            "form": form,
            "title": title
        })

    form = UserInfoModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/cover/')
    return render(request, 'register.html', {
        "form": form,
        "title": title
    })