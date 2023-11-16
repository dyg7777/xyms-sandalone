from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.utils import timezone
# Create your models here.

# 企业信息和授权信息
class Enterprise(models.Model):
    enter_name=models.CharField(max_length=255,null=False,blank=False,unique=True,default='',help_text='企业名称')
    enter_uncode = models.CharField(max_length=255,null=False,blank=False, default='', help_text='统一代码证号')
    enter_author_start_date=models.DateTimeField(default=timezone.now,null=False,blank=False,help_text='授权开始时间')
    enter_author_end_date=models.DateTimeField(default=timezone.now,null=False,blank=False,help_text='授权开始时间')
    enter_code=models.CharField(max_length=255, default="",null=False,blank=False, help_text='企业码')
    enter_author_code = models.CharField(max_length=255,null=False,blank=False, default="", help_text='授权码')
    enter_free_credit = models.IntegerField(max_length=5, null=False, blank=False,default=50,help_text='授权额度')
    version_number=models.CharField(max_length=255, null=False, blank=False, default='',help_text='版本号')


# 作用于软件内部的时间
class RunDate(models.Model):
    run_datetime=models.DateField(default=timezone.datetime.now,help_text='系统执行时间')
    real_datetime=models.DateTimeField(auto_now=True,help_text='真实时间')


# 用户权限
class UserPermissions(models.Model):
    permissions_name=models.CharField(max_length=255, null=False, blank=False,unique=True,help_text='权限名称')


# 用户库
class User(models.Model):
    username=models.CharField(max_length=255,null=False,blank=False,unique=True,default=make_password('鑫奕科创','980513','pdkdf2_sha1'),help_text='用户名')
    password = models.CharField(max_length=255, null=False,blank=False,default=make_password('15145181511','1975217','pbkdf2_sha1'), help_text='登录密码')
    show_name=models.CharField(max_length=255, null=False, blank=False,default='鑫奕科创',help_text='用来显示用户名信息')
    user_permissions = models.ForeignKey(UserPermissions,on_delete=models.CASCADE,related_name='userpremissions',help_text='用户权限')


# 程序目录
class ProgectPath(models.Model):
    path_name=models.CharField(max_length=255, null=False, blank=False,unique=True,default='',help_text='程序工作目录')


# 数据库目录
class DatabasePath(models.Model):
    host=models.CharField(max_length=255, null=False, blank=False, default='127.0.0.1',help_text='数据库连接地址')
    port=models.CharField(max_length=255, null=False, blank=False, default='3306',help_text='数据库端口号')
    db_name=models.CharField(max_length=255, null=False, blank=False,default='xyms_db',help_text='数据库名')
    user_name = models.CharField(max_length=255, null=False, blank=False,default='root',help_text='用户名')
    password = models.CharField(max_length=255, null=False, blank=False,default='',help_text='密码')
    charset = models.CharField(max_length=255, null=False, blank=False,default='utf-8',help_text='字符编码')


