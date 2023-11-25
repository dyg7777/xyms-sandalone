from django.db import models
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.utils import timezone
# Create your models here.

# 企业信息和授权信息


class Enterprise(models.Model):
    enter_name = models.CharField(
        max_length=255, null=False, blank=False, unique=True, default='', help_text='企业名称')
    enter_uncode = models.CharField(
        max_length=255, null=True, blank=True, default='', help_text='统一代码证号')
    enter_author_start_date = models.DateTimeField(
        null=True, blank=True, help_text='授权开始时间')
    enter_author_end_date = models.DateTimeField(
        null=True, blank=True, help_text='授权开始时间')
    enter_code = models.CharField(
        max_length=255, default="", null=True, blank=True, help_text='企业码')
    enter_author_code = models.CharField(
        max_length=255, null=True, blank=True, default="", help_text='授权码')
    enter_free_credit = models.IntegerField(
        null=True, blank=True, default=50, help_text='授权额度')
    version_number = models.CharField(
        max_length=255, null=True, blank=True, default='', help_text='版本号')
    app_name = models.CharField(
        max_length=255, default='', null=True, blank=True, help_text='授权使用软件名称')


# 作用于软件内部的时间
class RunDate(models.Model):
    run_datetime = models.DateTimeField(help_text='系统执行时间')
    real_datetime = models.DateTimeField(auto_now=True, help_text='本机时间')


# 用户权限
class UserPermissions(models.Model):
    permissions_code = models.CharField(
        max_length=10, null=True, blank=True, default='', help_text='权限ID')
    permissions_name = models.CharField(
        max_length=255, null=True, blank=True, unique=True, default='', help_text='权限名称')


# 用户库
class User_local(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True, unique=True, default=make_password(
        '鑫奕科创', salt='980513', hasher='default'), help_text='用户名')
    password = models.CharField(max_length=255, null=True, blank=True, default=make_password(
        '15145181511', salt='1975217', hasher="default"), help_text='登录密码')
    show_name = models.CharField(
        max_length=255, null=True, blank=True, default='鑫奕科创', help_text='用来显示用户名信息')
    user_permissions = models.CharField(
        max_length=50, null=True, blank=True, default='0000', help_text='用户权限')


# 程序目录
class ProgectPath(models.Model):
    projectfile_path = models.CharField(
        max_length=255, null=True, blank=True, unique=True, default='', help_text='程序工作目录')
    profiles_path = models.CharField(
        max_length=255, null=True, blank=True, unique=True, default='', help_text='配置文件目录')
    tempfiles_path = models.CharField(
        max_length=255, null=True, blank=True, unique=True, default='', help_text='临时文件目录')
    reportfile_path = models.CharField(
        max_length=255, null=True, blank=True, unique=True, default='', help_text='报表文件目录')
    resourcefile_path = models.CharField(
        max_length=255, null=True, blank=True, unique=True, default='', help_text='资源文件目录')

# 数据库目录


class DatabasePath(models.Model):
    host = models.CharField(max_length=255, null=True,
                            blank=True, default='127.0.0.1', help_text='数据库连接地址')
    port = models.CharField(max_length=255, null=True,
                            blank=True, default='3306', help_text='数据库端口号')
    db_name = models.CharField(
        max_length=255, null=True, blank=True, default='xyms_db', help_text='数据库名')
    user_name = models.CharField(
        max_length=255, null=True, blank=True, default='root', help_text='用户名')
    password = models.CharField(
        max_length=255, null=True, blank=True, default='53169549', help_text='密码')
    charset = models.CharField(
        max_length=255, null=True, blank=True, default='utf-8', help_text='字符编码')
