# Generated by Django 4.1.5 on 2023-01-06 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moble', models.CharField(max_length=11, verbose_name='手机号')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[(1, '一级'), (2, '二级'), (3, '三级')], default=1, verbose_name='等级')),
                ('status', models.SmallIntegerField(choices=[(1, '未售出'), (2, '已售出')], default=1, verbose_name='状态')),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department', verbose_name='部门'),
        ),
    ]
