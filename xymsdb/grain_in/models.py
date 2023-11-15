from django.db import models

# Create your models here.


# 货权人信息
class OwnerForGoods(models.Model):
    ownerforgoods_name=models.CharField(max_length=255,blank=False,null=True,default='企业私有',help_text='货权人名称')
    ownerforgoods_uncode=models.CharField(max_length=100,blank=False,null=True,default='',help_text='货权人代码')
    ownerforgoods_phonenumber=models.CharField(max_length=100,blank=False,null=True,default='',help_text='货权人联系方式')
    co_owners=models.CharField(max_length=255,blank=False,null=True,default='',help_text='货物共有人')


# 收购品种
class AcquisitionVarieties(models.Model):
    AV_name=models.CharField(max_length=255, blank=False, null=True,default='玉米',help_text='收购品种')
    acquisitioncaps = models.DecimalField(max_digits=12 ,decimal_places=4,help_text='收购上限')


# 收购国标
class GBInformations(models.Model):
    acquisitionVarietiesid=models.ForeignKey(AcquisitionVarieties,related_name='acquisition_varities',on_delete=models.CASCADE,help_text='收购品种库ID')
    GB_filename = models.CharField(max_length=255, blank=False, null=True,help_text='国标文件号')
    GB_file_contents=models.TextField(blank=False,null=True,default='',help_text='文件内容')
    