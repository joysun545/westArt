from django.shortcuts import render, redirect

from artWorks import models
from artWorks.views.user import UserResetModelForm


def reset(request, nid):
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

        return render(request, 'reset.html', context)
    form = UserResetModelForm(data=request.POST, instance=row_object)
    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():
        form.save()
        return redirect('/cover/')
    return render(request, 'reset.html', context)
