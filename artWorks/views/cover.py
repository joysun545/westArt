from django.http import JsonResponse
from django.shortcuts import render

from artWorks import models
from artWorks.utils.pagination import Pagination_lucent


def web_cover(request):
    """Web封面"""
    return render(request, 'cover.html')

def cover_completeworks(request):
    """封面 | 作品列表"""
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
        data_dict["name__contains"] = search_data
    # 根据搜索条件到数据库获取filter(**search_data)
    queryset = models.CompleteWorksInfo.objects.filter(**data_dict)

    page_object = Pagination_lucent(request, queryset, page_size=5)
    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, 'cover_completeworks.html', context)


def chart_list(request):
    """数据统计列表"""
    return render(request, 'cover_datan.html')


def chart_bar(request):
    """构造柱状图的数据"""

    legend = ['周光兵', '周灯润', '徐洪']
    series_list = [
        {
            "name": '周光兵',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 50]
        },
        {
            "name": '周灯润',
            "type": 'bar',
            "data": [22, 25, 16, 20, 15, 15]
        },
        {
            "name": '徐洪',
            "type": 'bar',
            "data": [22, 15, 16, 20, 25, 5]
        }
    ]
    x_axis = ['一月', '二月', '三月', '四月', '五月', '六月']

    result = {
        "status": True,
        "data": {
            "legend": legend,
            "series_list": series_list,
            "x_axis": x_axis
        }
    }
    return JsonResponse(result)


def chart_pie(request):
    """构造饼状图的数据"""
    db_data_list = [
        {"value": 1048, "name": 'Search Engine'},
        {"value": 735, "name": 'Direct'},
        {"value": 580, "name": 'Email'},
        {"value": 484, "name": 'Union Ads'},
        {"value": 300, "name": 'Video Ads'},
    ]
    result = {
        "status": True,
        "data": db_data_list,
    }
    return JsonResponse(result)

