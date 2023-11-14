from django.db import models

# Create your models here.


# 货权人信息
class OwnerForGoods(models.Model):
    ownerforgoods_name=models.CharField(max_length=255,blank=False,null=True,default='企业私有',help_text='货权人名称')
    ownerforgoods_uncode=models.CharField(max_length=100,blank=False,null=True,default='',help_text='货权人代码')
    ownerforgoods_phonenumber=models.CharField(max_length=100,blank=False,null=True,default='',help_text='货权人联系方式')
    co_owners=models.CharField(max_length=255,blank=False,null=True,help_text='货物共有人')
    