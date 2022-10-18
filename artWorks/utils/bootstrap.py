"""创建一个CSS格式form插件，供其他form调用"""

from django import forms



class BootStrap:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class":"form-control",
                    "placeholder":field.label
                }



class BootstrapModelForm(BootStrap,forms.ModelForm):
    pass
    # def __init__(self, *args, **kwargs):
    #     """初始化样式插件"""
    #
    #     super().__init__(*args, **kwargs)
    #
    #     # 循环为所有的对象（name,password,age,....），添加class="form-control"样式
    #     for name, field in self.fields.items():
    #         if field.widget.attrs:
    #             field.widget.attrs["class"] = "form-control"
    #             field.widget.attrs["placeholder"] = field.label
    #         else:
    #             field.widget.attrs = {
    #                 "class": "form-control",
    #                 "placeholder": field.label
    #             }  # 可以添加你需要的样式 class style ....


class BootstrapForm(BootStrap, forms.Form):
    pass