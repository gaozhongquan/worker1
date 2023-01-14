from django.shortcuts import render, redirect
from app import models
from app.utils.ModerForm import UserModerForm


def user_list(request):
    queryset = models.UserInfo.objects.all()
    return render(request, "user_list.html", {"queryset": queryset})


def user_add(request):
    if request.method == "GET":
        depart_list = models.Department.objects.all()
        gender_choices = models.UserInfo.gender_choices
        return render(request, "user_add.html", {"depart_list": depart_list, "gender_choices": gender_choices})
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        age = request.POST.get("age")
        ac = request.POST.get("ac")
        ctime = request.POST.get("ctime")
        gd = request.POST.get("gd")
        dp = request.POST.get("dp")
        models.UserInfo.objects.create(name=user, password=pwd, age=age, account=ac, create_time=ctime, gender=gd,
                                       depart_id=dp)
        return redirect('/user_list/')


def user_add_model(request):
    if request.method == "GET":
        form = UserModerForm()
        return render(request, "form.html", {"form": form, "title": "添加用户"})
    else:
        form = UserModerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/user_list/")
        else:
            return render(request, "form.html", {"form": form, "title": "添加用户"})


def user_eidt(request, nid):
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModerForm(instance=row_object)
        return render(request, "form.html", {"form": form, "title": "编辑用户"})
    else:
        form = UserModerForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/user_list/")
        else:
            return render(request, "form.html", {"form": form, "title": "编辑用户"})


def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user_list/")