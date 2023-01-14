from django.core.exceptions import ValidationError
from django.forms import forms

from app import models
from app.utils.bootstrap import BootStrap
from app.utils.encrypt import md5

class DepartModerForm(BootStrap,forms.ModelForm):
    class Meta:
        model = models.Department
        fields = "__all__"


class UserModerForm(BootStrap,forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "depart", "gender"]
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     for name, field in self.fields.item():
        #         field.widgets.attrs = {"class": "form-contorl", "placehoder": field.label}


class PrettyNumUserModerForm(BootStrap, forms.ModelForm):
    #  model = forms.CharField(label="手机号", validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号输入有误')])
    class Meta:
        model = models.PrettyNum
        fields = ["moble", "price", "level", "status"]
        # fields = "__all__"  所有字段
        # exclude = ["level"] 排除字段

    def clean_moble(self):  # 钩子方法用于校验数据存入存入数据库
        txt_moble = self.cleaned_data["moble"]
        if len(txt_moble) != 11:
            raise ValidationError("验证不通过")
        return txt_moble


class PrettynumEidtModerForm(BootStrap,forms.ModelForm):
    # moble = forms.CharField(disabled=True, label="手机号")
    class Meta:
        model = models.PrettyNum
        fields = ["moble", "price", "level", "status"]

    def clean_moble(self):
        txt_moble = self.cleaned_data["moble"]
        exist = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(moble=txt_moble).exists()
        if exist:
            raise ValidationError("手机号已存在")
        else:
            return txt_moble

class AdminModerForm(BootStrap, forms.ModelForm):
    confirm_password = forms.CharField(label="确认密码",widget=forms.PasswordInput(render_value=True))
    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]
        widgets= {"password": forms.PasswordInput(render_value=True)}
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("密码相同")
        else:
            return md5_pwd
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if pwd != confirm:
            raise ValidationError("密码不一致")
        return confirm
class AdminEidtModerForm(BootStrap, forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ["username"]

class AdminAddModelForm(BootStrap, forms.ModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["username", 'password', "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)
