from re import T
from django.db import models

# Create your models here.


# 货权人信息
class OwnerForGoods(models.Model):
    ownerforgoods_name=models.CharField(max_length=255,blank=False,null=True,unique=True,default='企业私有',help_text='货权人名称')
    ownerforgoods_uncode=models.CharField(max_length=100,blank=False,null=True,default='',help_text='货权人代码')
    ownerforgoods_phonenumber=models.CharField(max_length=100,blank=False,null=True,default='',help_text='货权人联系方式')
    co_owners=models.CharField(max_length=255,blank=False,null=True,help_text='货物共有人')

# 发货品种
class AcquisitionVarieties(models.Model):
    AV_name=models.CharField(max_length=255, blank=False, null=True,default='玉米',unique=True,help_text='发货品种')
    find_code = models.CharField(max_length=255, blank=False, null=True,unique=True,default='',help_text='查询编码')
    py_abbreviation=models.CharField(max_length=255,blank=False,null=True,unique=False,default='',help_text='拼音简写')
    acquisitioncaps = models.DecimalField(max_digits=12 ,decimal_places=4,help_text='发货上限')