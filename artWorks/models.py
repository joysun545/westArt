from django.db import models


class AdminInfo(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    # 定义以下函数，可以让调用是直接显示“管理员姓名”
    def __str__(self):
        return self.username


class ArtCategoryInfo(models.Model):
    """艺术门类"""

    category = models.CharField(verbose_name="艺术门类", max_length=12)

    def __str__(self):
        return self.category


class ArtistInfo(models.Model):
    """艺术家信息"""
    name = models.CharField(verbose_name="姓名", max_length=32)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    # SmallIntegerField-小整数（1,2）
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, null=True)
    birthtime = models.DateField(verbose_name="出生时间", max_length=12, null=True)
    birthplace = models.CharField(verbose_name="出生地", max_length=64, null=True)
    # to-关联表   to_fields-关联列   on_delete=models.CASCADE 级联删除
    artrategory = models.ForeignKey(verbose_name="艺术门类", to="ArtCategoryInfo", null=True, to_field="id",
                                    on_delete=models.CASCADE)
    # null=True,blank=True, on_delete=models.SET_NULL 置空
    # department = models.ForeignKey(to="Department", to_fields="id", null=True,blank=True, on_delete=models.SET_NULL)
    artschools = models.ForeignKey(verbose_name="艺术流派", to="SchoolsInfo", null=True, blank=True, to_field="id",
                                   on_delete=models.CASCADE)

    def __str__(self):
        """解决modelform输出是一对象department object(id)而不是文字字符串"""
        return self.name


class CompleteWorksInfo(models.Model):
    """艺术作品大全"""

    name = models.CharField(verbose_name="艺术品名称", max_length=32)
    artistname = models.CharField(verbose_name="艺术家姓名", max_length=32, null=True)
    artcreationtype = models.CharField(verbose_name="创作类型", max_length=16, null=True)
    creationtime = models.CharField(verbose_name="创作时间", max_length=32, null=True)
    collectionmuseum = models.CharField(verbose_name="收藏博物馆", max_length=32, null=True)
    uploadtime = models.DateField(verbose_name="上传时间", null=True)
    sharer = models.ForeignKey(verbose_name="分享者",to="UserInfo",on_delete=models.CASCADE,null=True)
    # sharer = models.CharField(verbose_name="分享者", max_length=12,null=True)


class CreationTypeInfo(models.Model):
    """创作形类型"""
    creationtype = models.CharField(verbose_name="创作类型", max_length=16)
    category = models.ForeignKey(verbose_name="艺术门类", to="ArtCategoryInfo", null=True, to_field="id",
                                 on_delete=models.CASCADE)

    def __str__(self):
        """解决modelform输出是一对象creationtype object(id)而不是文字字符串"""
        return self.creationtype


class MuseumInfo(models.Model):
    name = models.CharField(verbose_name="博物馆名称", max_length=32)
    country = models.CharField(verbose_name="博物馆所在国家", max_length=16)
    city = models.CharField(verbose_name="博物馆所在城市", max_length=32)

    def __str__(self):
        """解决modelform输出是一对象department object(id)而不是文字字符串"""
        return self.name


class SchoolsInfo(models.Model):
    """艺术流派"""
    schools = models.CharField(verbose_name="流派", max_length=32)
    artcategory = models.ForeignKey(verbose_name="艺术门类", to="ArtCategoryInfo", null=True, to_field="id",
                                    on_delete=models.CASCADE)

    def __str__(self):
        """解决modelform输出是一对象department object(id)而不是文字字符串"""
        return self.schools


class UserInfo(models.Model):
    """用户信息"""
    username = models.CharField(verbose_name="昵称", max_length=16, null=True)
    name = models.CharField(verbose_name="姓名", max_length=16, null=True)
    password = models.CharField(verbose_name="密码", max_length=64, null=True)
    mobile = models.CharField(verbose_name="手机号", max_length=11, null=True)
    email = models.EmailField(verbose_name="邮箱", null=True)
    birthtime = models.DateField(verbose_name="年龄", null=True)
    country = models.CharField(verbose_name="国家", max_length=16, null=True)
    city = models.CharField(verbose_name="城市", max_length=16, null=True)
    graduated = models.CharField(verbose_name="毕业院校", max_length=32, null=True)
    artcategory = models.ForeignKey(verbose_name="艺术门类", to="ArtCategoryInfo", null=True, to_field="id",
                                    on_delete=models.CASCADE)
    saysomethingmore = models.TextField(verbose_name="再说点什么",max_length=280,null=True)

    # 在django中作的约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    # SmallIntegerField-小整数（1,2）
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, null=True)

    def __str__(self):
        """解决modelform输出是一对象name object(id)而不是文字字符串"""
        return self.username
