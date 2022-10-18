from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, queryset, page_size=5, page_param="page", plus=5):
        """
        
        :param request: 请求的对象
        :param queryset: 符合条件的数据（根据这个数据给它进行分页处理）
        :param page_size: 每页显示多少条数据
        :param page_param: 在URL中传递的获取分页的参数，例如：/etty/list/?page=12
        :param plus: 显示当前也的前或后几页（页码）
        """

        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]

        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 计算出，显示当前页的前5页,后5页
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库中的数据较少，不足11页
            start_page = 1
            end_page = self.total_page_count
        else:
            # 数据库中的数据较多 > 11页
            # 当前页小于5
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页大于5
                # 当前页+5>总页数
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页面
        page_str_list = []

        self.query_dict.setlist(self.page_param, [1])
        print(self.query_dict.urlencode())

        page_str_list.append(
            '<li><a href="?{}">首页</a></li>'.format(
                self.query_dict.urlencode()))

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(
                self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(
                self.query_dict.urlencode())
        page_str_list.append(prev)

        # 页面
        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}">下一页</a></li>'.format(
                self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}">下一页</a></li>'.format(
                self.query_dict.urlencode())
        page_str_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append(
            '<li><a href="?{}">尾页</a></li>'.format(
                self.query_dict.urlencode()))

        search_string = """
            <li>
                <form style="float:left;margin-left:-1px;" method="get">
                    <input name="page"
                        style="position:relative;float:left;display:inline-block;width:88px;border-radius:0"
                        type="text" class="form-control" placeholder="页码">
                    <button style="border-radius:0;" class="btn btn-default" type="submit">跳转</button>
                </form>
            </li>
            """

        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string


class Pagination_lucent(object):
    def __init__(self, request, queryset, page_size=5, page_param="page", plus=5):
        """

        :param request: 请求的对象
        :param queryset: 符合条件的数据（根据这个数据给它进行分页处理）
        :param page_size: 每页显示多少条数据
        :param page_param: 在URL中传递的获取分页的参数，例如：/etty/list/?page=12
        :param plus: 显示当前也的前或后几页（页码）
        """

        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]

        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 计算出，显示当前页的前5页,后5页
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库中的数据较少，不足11页
            start_page = 1
            end_page = self.total_page_count
        else:
            # 数据库中的数据较多 > 11页
            # 当前页小于5
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页大于5
                # 当前页+5>总页数
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页面
        page_str_list = []

        self.query_dict.setlist(self.page_param, [1])
        print(self.query_dict.urlencode())

        page_str_list.append(
            '<li><a href="?{}" style="background: hsla(0, 0%, 50%, .25) border-box;">首页</a></li>'.format(
                self.query_dict.urlencode()))

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}" style="background: hsla(0, 0%, 50%, .25) border-box;">上一页</a></li>'.format(
                self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}" style="background: hsla(0, 0%, 50%, .25) border-box;">上一页</a></li>'.format(
                self.query_dict.urlencode())
        page_str_list.append(prev)

        # 页面
        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}" style="background: hsla(0, 0%, 50%, .25) border-box;border-color:white;">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}" style="background: hsla(0, 0%, 50%, .25) border-box;">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}" style="background: hsla(0, 0%, 50%, .25) border-box;">下一页</a></li>'.format(
                self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}" style="background: hsla(0, 0%, 50%, .25) border-box;">下一页</a></li>'.format(
                self.query_dict.urlencode())
        page_str_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append(
            '<li><a href="?{}" style="background: hsla(0, 0%, 50%, .25) border-box;">尾页</a></li>'.format(
                self.query_dict.urlencode()))

        search_string = """
            <li>
                <form style="float:left;margin-left:-1px;" method="get">
                    <input name="page"
                        style="position:relative;background: hsla(0, 0%, 50%, .25) border-box;float:left;display:inline-block;width:88px;border-radius:0"
                        type="text" class="form-control" placeholder="页码">
                    <button style="border-radius:0;background: hsla(0, 0%, 50%, .25) border-box;" class="btn btn-default" type="submit">跳转</button>
                </form>
            </li>
            """

        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string

