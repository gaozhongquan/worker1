from django.shortcuts import render, redirect, HttpResponse
from django import forms
from app.utils.ModerForm import BootStrap
from app.utils.encrypt import md5
from app import models
class LoginForm(BootStrap, forms.Form):
     username = forms.CharField(label="用户名",
                                required= True)
     password = forms.CharField(label="密码",
                                widget=forms.PasswordInput(render_value=True),
                                required=True
                                )
     def clean_password(self):
         pwd = self.cleaned_data.get("password")
         return md5(pwd)
def login (request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,"login.html", {"form": form})
    else:
        form: LoginForm = LoginForm(data=request.POST)
        if form.is_valid():
            admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
            if admin_object:
                request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
                return redirect("/admin_list/")
            else:
                form.add_error("password", "用户名或者密码错误")
                return render(request,"login.html", {"form": form})

        else:
            return render(request, "login.html", {"form": form})