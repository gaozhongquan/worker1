from django.shortcuts import render, redirect
from app import models
from app.utils.pagination import Pagination
from app.utils.ModerForm import PrettynumEidtModerForm, PrettyNumUserModerForm


def prettynum_list(request):
    # dic = {"moble": "15629110332", "id":1}
    # q = models.PrettyNum.objects.filter(**dic) (**dic)= (key, values)
    # print(q)
    # # 整形
    # models.PrettyNum.objects.filter(id=12)  #等于12
    # models.PrettyNum.objects.filter(id__ge=12) #大于12
    # models.PrettyNum.objects.filter(id__gte =12) #大于等于12
    # models.PrettyNum.objects.filter(id__lt=12) #小于12
    # models.PrettyNum.objects.filter(id__let=12) #小于等于12
    # # 字符串
    # models.PrettyNum.objects.filter(moble__startswith="1111") #以1111开头
    # models.PrettyNum.objects.filter(moble__endswith="1111") #以1111结尾
    # models.PrettyNum.objects.filter(moble__contains="1111") #包含1111
    # for i in range(0,1000):
    #     models.PrettyNum.objects.filter(moble__contains=176).delete()
    dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        dict["moble__contains"] = search_data
    queryset = models.PrettyNum.objects.filter(**dict).order_by("-level")
    page = Pagination(request, queryset)
    context = {"data": page.queryset, "page_string": page.html()}
    return render(request, "prettynum_list.html", context)


def prettynum_add(request):
    if request.method == 'GET':
        form = PrettyNumUserModerForm()
        return render(request, "form.html", {"form": form, "title": "添加靓号"})
    else:
        form = PrettyNumUserModerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/prettynum_list/")
        else:
            return render(request, "form.html", {"form": form, "title": "添加靓号"})


def prettynum_eidt(request, nid):
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PrettynumEidtModerForm(instance=row_object)
        return render(request, "form.html", {"form": form, "title": "修改靓号"})
    else:
        form = PrettynumEidtModerForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/prettynum_list/")
        else:
            return render(request, "form.html", {"form": form, "title": "修改靓号"})


def prettynum_del (request, nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/prettynum_list/")