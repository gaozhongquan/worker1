"""worker URL Configuration

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app.view import depart, user, prettynum, admin, account
urlpatterns = [
    # path('admin/', admin.site.urls),
    #部门管理
    path('depart_list/', depart.depart_list),
    path('depart_add/', depart.depart_add),
    path('depart_del_<int:nid>/', depart.depart_del),
    path('depart_eidt_<int:nid>/', depart.depart_eidt),


    #用户管理
    path('user_list/', user.user_list),
    path('user_add/', user.user_add),
    path('user_add_model/', user.user_add_model),
    path('user_eidt_<int:nid>/', user.user_eidt),
    path('user_del_<int:nid>/', user.user_del),


    # 靓号管理
    path('prettynum_list/', prettynum.prettynum_list),
    path('prettynum_add/', prettynum.prettynum_add),
    path('prettynum_eidt_<int:nid>/', prettynum.prettynum_eidt),
    path('prettynum_del_<int:nid>/', prettynum.prettynum_del),


    # 管理员的管理
    path('admin_list/', admin.admin_list),
    path('admin_add/', admin.admin_add),
    path('admin_eidt_<int:nid>/', admin.admin_eidt),
    path('admin_reset_<int:nid>/', admin.admin_reset),
    path('admin_del_<int:nid>/', admin.admin_del),

    # 登陆管理
    path('login/', account.login),
]
