from django.db import models

class Department(models.Model):
    """部门表"""
    title =  models.CharField(verbose_name="标题", max_length=32)
    def __str__(self):
        return self.title
class UserInfo(models.Model):
    """员工表 """
    name = models.CharField(verbose_name="姓名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name="余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")
    # create_time = models.DateField(verbose_name="入职时间")
    depart = models.ForeignKey(to='Department', verbose_name="部门", to_field="id", on_delete=models.CASCADE)
    gender_choices = (
        (1,'男'),
        (2,'女'),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
class PrettyNum(models.Model):
    moble = models.CharField(verbose_name="手机号", max_length=11)
    price = models.IntegerField(verbose_name="价格")
    level_choices = (
        (1, "一级"),
        (2, "二级"),
        (3, "三级"),
    )
    level = models.SmallIntegerField(verbose_name="等级", choices=level_choices, default=1)
    status_choices = (
        (1, "未售出"),
        (2, "已售出"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
class Admin (models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)