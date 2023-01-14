from django.shortcuts import render, redirect
from app import models
from app.utils.ModerForm import DepartModerForm

def depart_list(request):
    queryset = models.Department.objects.all()
    return render(request,'depart_list.html', {"queryset": queryset})


def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        form = DepartModerForm()
        return render(request, "form.html", {"form": form, "title": "添加部门"})
    else:
        form = DepartModerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/depart_list/")
        else:
             return render(request, "form.html", {"form": form, "title": "添加部门"})
        # title = request.POST.get("title")
        # models.Department.objects.create(title=title)
        # return redirect("/depart_list/")


def depart_del(request, nid):
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart_list/")


def depart_eidt(request, nid):
    row_object = models.Department.objects.filter(id=nid).first()
    print(row_object)
    if request.method == "GET":
        form = DepartModerForm(instance=row_object)
        # print(title)
        return render(request, "form.html", {"form": form, "title": "修改部门"})
    else:
        form = DepartModerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/depart_list/")
        else:
            return render(request, "form.html", {"form": form, "title": "修改部门"})
        # title = request.POST.get("title")
        # models.Department.objects.filter(id=nid).update(title=title)
        # return redirect("/depart_list/")