# Generated by Django 4.2.7 on 2023-12-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_login_logs_login_enter_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_logs',
            name='login_dev_uuid',
            field=models.CharField(blank=True, default='', help_text='登录设备ID,第一次登录创建后不换系统永久有效', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='login_logs',
            name='logout_time',
            field=models.DateTimeField(auto_now=True, help_text='最后操作或者登出时间'),
        ),
        migrations.AlterField(
            model_name='login_logs',
            name='return_uuid',
            field=models.CharField(blank=True, default='', help_text='返回前端登录识别码', max_length=100, null=True),
        ),
    ]
