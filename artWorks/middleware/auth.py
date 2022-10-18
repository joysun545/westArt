"""中间件"""
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddelware(MiddlewareMixin):
    """中间件1"""

    def process_request(self, request):

        if request.path_info in ['/login/', '/image/code/', '/register/', '/cover/', '/cover/completeworks/',
                                 '/chart/list/', '/admin/','/admin/login/?next=/admin/']:
            return

        # 读取当前访问的用户的session信息，如果能读到，说明登录过，就可以继续往下走
        info_dict = request.session.get('info')
        if info_dict:
            return

        return redirect('/login/')
