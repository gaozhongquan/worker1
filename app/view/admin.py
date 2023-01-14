from django.shortcuts import render, redirect
from app import models
from app.utils.ModerForm import AdminModerForm, AdminAddModelForm, AdminEidtModerForm
from app.utils.pagination import Pagination
from django.core.exceptions import ValidationError


def admin_list(request) :
    dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        dict["username"]=search_data
    queryset = models.Admin.objects.filter(**dict)
    page = Pagination(request,queryset)
    context = {"data": page.queryset, "page_string": page.html()}
    return render(request, "admin_list.html",context)
def admin_add (request):
    if request.method == "GET":
        form = AdminAddModelForm()
        return render(request, "form.html", {"form": form, "title": "添加管理员"})
    else:
        form = AdminAddModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/admin_list/")
        else:
            return render(request, "form.html", {"form": form, "title": "添加管理员"})
def admin_eidt(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if request.method == "GET":
        form = AdminEidtModerForm(instance=row_object)
        return render(request, "form.html", {"form": form, "title": "修改管理员"})
    else:
        form = AdminEidtModerForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/admin_list/")
        else:
            return render(request, "form.html", {"form": form, "title": "添加管理员"})


def admin_reset (request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if row_object == None:
        raise ValidationError("无此账号")
    else:
        if request.method == "GET":
            form = AdminModerForm()
            return render(request, "form.html", {"form": form, "title": "添加管理员——{}".format(row_object.username)})
        else:
            form = AdminModerForm(data=request.POST, instance=row_object)
            if form.is_valid():
                form.save()
                return redirect("/admin_list/")
            else:
                return render(request, "form.html", {"form": form, "title": "添加管理员——{}".format(row_object.username)})


def admin_del (request, nid) :
    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin_list")