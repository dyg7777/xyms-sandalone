from django.db import models
from django.contrib.auth.models import make_password
from django.utils import timezone
# Create your models here.


class Enterprise(models.Model):
    enter_name=models.CharField(max_length=255,null=True,blank=False,default='',help_text='企业名称')
    enter_uncode = models.CharField(max_length=255,null=True,blank=False, default='', help_text='统一代码证号')
    enter_author_start_date=models.DateTimeField(default=timezone.now,null=True,blank=False,help_text='授权开始时间')
    enter_author_end_date=models.DateTimeField(default=timezone.now,null=True,blank=False,help_text='授权开始时间')
    enter_code=models.CharField(max_length=255, default="",null=True,blank=False, help_text='企业码')
    enter_author_code = models.CharField(max_length=255,null=True,blank=False, default="", help_text='授权码')
    enter_free_credit = models.IntegerField(max_length=5, null=True, blank=False,default=50,help_text='授权额度')

class RunDate(models.Model):
    run_date=models.DateField(default=timezone.datetime.now,help_text='系统执行时间')




class User(models.Model):
    username=models.CharField(max_length=255,null=True,blank=False,default='鑫奕科创',help_text='用户名')
    password = models.CharField(max_length=255, null=True,blank=False,default=make_password('15145181511'), help_text='登录密码')
