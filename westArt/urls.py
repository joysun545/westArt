"""westArt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from artWorks import views
from artWorks.views import cover, normal_admin, user, creationtype, artcategory, artist, schools, museum, completeworks, \
    datan, \
    login, register, reset, userinfo, completeworks02

urlpatterns = [
    path('admin/', admin.site.urls),
    # 封面
    path('cover/', cover.web_cover),
    path('cover/completeworks/', cover.cover_completeworks),
    path('chart/list/', cover.chart_list),
    path('chart/bar/', cover.chart_bar),
    path('chart/pie/', cover.chart_pie),

    # 管理员列表
    path('admin/list/', normal_admin.admin_list),
    path('admin/add/', normal_admin.admin_add),
    path('admin/<int:nid>/edit/', normal_admin.admin_edit),
    path('admin/<int:nid>/delete/', normal_admin.admin_delete),
    path('admin/<int:nid>/reset/', normal_admin.admin_reset),
    # 用户登录
    path('login/', login.login),
    path('logout/', login.logout),
    path('image/code/', login.image_code),
    # 重置密码
    path('reset/<int:nid>/reset/',reset.reset),
    # 用户注册
    path('register/', register.user_register),
    # 用户列表
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),
    path('user/<int:nid>/reset/',user.user_reset),
    # 创作类型列表
    path('creationtype/list/', creationtype.creationtype_list),
    path('creationtype/add/', creationtype.creationtype_add),
    path('creationtype/<int:nid>/edit/', creationtype.creationtype_edit),
    path('creationtype/<int:nid>/delete/', creationtype.creationtype_delete),
    # 艺术领域列表
    path('artcategory/list/', artcategory.artcategory_list),
    path('artcategory/add/', artcategory.artcategory_add),
    path('artcategory/<int:nid>/edit/', artcategory.artcategory_edit),
    path('artcategory/<int:nid>/delete/', artcategory.artcategory_delete),
    # 艺术家列表
    path('artist/list/', artist.artist_list),
    path('artist/add/', artist.artist_add),
    path('artist/<int:nid>/edit/', artist.artist_edit),
    path('artist/<int:nid>/delete/', artist.artist_delete),
    # 艺术流派列表
    path('schools/list/', schools.schools_list),
    path('schools/add/', schools.schools_add),
    path('schools/<int:nid>/edit/', schools.schools_edit),
    path('schools/<int:nid>/delete/', schools.schools_delete),
    # 博物馆列表
    path('museum/list/', museum.museum_list),
    path('museum/add/', museum.museum_add),
    path('museum/<int:nid>/edit/', museum.museum_edit),
    path('museum/<int:nid>/delete/', museum.museum_delete),
    # 艺术作品大全列表
    path('completeworks/list/', completeworks.completeworks_list),
    path('completeworks/add/', completeworks.completeworks_add),
    path('completeworks/<int:nid>/edit/', completeworks.completeworks_edit),
    path('completeworks/<int:nid>/delete/', completeworks.completeworks_delete),
    # 数据统计
    path('datan/list/', datan.datan_list),
    # 用户信息详情
    path('userinfo/<int:nid>/details/',userinfo.userinfo_details),
    path('userinfo/<int:nid>/edit/',userinfo.userinfo_edit),
# 艺术作品大全列表
    path('completeworks02/list/', completeworks02.completeworks02_list),
    path('completeworks02/add/', completeworks02.completeworks02_add),
    path('completeworks02/<int:nid>/detail/', completeworks02.completeworks02_detail),
    path('completeworks02/<int:nid>/delete/', completeworks02.completeworks02_delete),
    path('completeworks02/<int:nid>/edit/', completeworks02.completeworks02_edit),

]
