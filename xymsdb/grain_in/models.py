from django.db import models

# Create your models here.


# 货权人信息
class OwnerForGoods(models.Model):
    ownerforgoods_name=models.CharField(max_length=255,blank=False,null=True,unique=True,default='企业私有',help_text='货权人名称')
    ownerforgoods_uncode=models.CharField(max_length=100,blank=False,null=True,default='',help_text='货权人代码')
    ownerforgoods_phonenumber=models.CharField(max_length=100,blank=False,null=True,default='',help_text='货权人联系方式')
    co_owners=models.CharField(max_length=255,blank=False,null=True,default='',help_text='货物共有人')


# 收购品种
class AcquisitionVarieties(models.Model):
    AV_name=models.CharField(max_length=255, blank=False, null=True,unique=True,default='玉米',help_text='收购品种')
    find_code = models.CharField(max_length=255, blank=False, null=True,unique=True,default='',help_text='查询编码')
    py_abbreviation=models.CharField(max_length=255,blank=False,null=True,unique=False,default='',help_text='拼音简写')
    acquisitioncaps = models.DecimalField(max_digits=12 ,decimal_places=4,help_text='收购上限')


# 收购国标
class GBInformations(models.Model):
    acquisitionVarietiesid=models.ForeignKey(AcquisitionVarieties,related_name='acquisition_varities',on_delete=models.CASCADE,help_text='收购品种库ID')
    GB_filename = models.CharField(max_length=255, blank=False, null=True,help_text='国标文件号')
    GB_file_contents=models.TextField(blank=False,null=True,default='',help_text='文件内容')
    purchase_price=models.DecimalField(max_digits=12,decimal_places=6,help_text='等级价格')
    purchase_name = models.CharField(max_length=255, blank=False, null=True,unique=True,default="",help_text='等级名称')
    test_weight_high=models.DecimalField(max_digits=6, decimal_places=1, help_text="容重上限3.1")
    test_weight_low=models.DecimalField(max_digits=6, decimal_places=1, help_text="容重下限3.1")
    defective_kernels=models.DecimalField(max_digits=6,decimal_places=1,help_text='不完善粒标准3.2')
    insect_damaged_kernels=models.DecimalField(max_digits=6,decimal_places=1,help_text='虫蚀粒标准3.2.1')
    spotted_kernels=models.DecimalField(max_digits=6,decimal_places=1,help_text='病斑粒标准3.2.2')
    broken_kernels=models.DecimalField(max_digits=6,decimal_places=1,help_text='破损粒标准3.2.3')
    sprouted_kernels = models.DecimalField(max_digits=6, decimal_places=1,help_text='生芽粒标准3.2.4')
    moldy_kernels=models.DecimalField(max_digits=6,decimal_places=1,help_text='生霉粒标准3.2.5')
    heat_damaged_kernels = models.DecimalField(max_digits=6, decimal_places=1, help_text='热损伤粒标准3.2.6')
    nature_heat_damaged_kernels = models.DecimalField(max_digits=6, decimal_places=1,help_text='自然热损伤粒标准3.2.6.1')
    drying_heat_damaged_kernels=models.DecimalField(max_digits=6, decimal_places=1,help_text='烘干热损伤粒标准3.2.6.2')
    foreign_matter=models.DecimalField(max_digits=6,decimal_places=1,help_text='杂质标准3.3')
    throughs = models.DecimalField(max_digits=6, decimal_places=1, help_text='筛下物标准3.3.1')
    inorganic_impurities=models.DecimalField(max_digits=6, decimal_places=1, help_text='无机杂质3.3.2')
    organic_impurities = models.DecimalField(max_digits=6, decimal_places=1, help_text='有机杂质3.3.3')
    colour=models.CharField(max_length=50,default='正常',help_text='色泽3.4')
    odour=models.CharField(max_length=50, default="<empty>", help_text='气味3.5')
    moisture_content=models.DecimalField(max_digits=6,decimal_places=1,help_text='水份标准3.6')
    severely_moldy_kernels=models.DecimalField(max_digits=6,decimal_places=1,help_text='霉变粒标准3.7')
   

# 水份定价表
class MoisturePrice(models.Model):
    varieties_id=models.ForeignKey(AcquisitionVarieties,on_delete=models.CASCADE,help_text='品种ID')
    purchase_id=models.ForeignKey(GBInformations,on_delete=models.DO_NOTHING,help_text='等级标准')
    moisture=models.DecimalField(max_digits=7, decimal_places=4, help_text="水份值")
    price=models.DecimalField(max_digits=7, decimal_places=4, help_text="水份对应价格")



# 包装物设置
class Packaging(models.Model):
    packag_name = models.CharField(max_length=255, blank=False, null=True,default='散积',unique=True,help_text='包装物名称')
    find_code = models.CharField(max_length=255, blank=False, null=True,unique=True,default='',help_text='查询编码')
    py_abbreviation=models.CharField(max_length=255,blank=False,null=True,unique=False,default='',help_text='拼音简写')


# 车种设置
class VehicleType(models.Model):
    vehicle_type=models.CharField(max_length=255, blank=False, null=True,unique=True,default='',help_text='车辆类型')
    find_code = models.CharField(max_length=255, blank=False, null=True,unique=True,default='',help_text='查询编码')
    py_abbreviation=models.CharField(max_length=255,blank=False,null=True,unique=False,default='',help_text='拼音简写')


# 货位仓号
class LocationWarehouseNumber(models.Model):
    location_number = models.CharField(max_length=255, blank=False, null=True,unique=True,default='',help_text='仓号')
    warehouse_number=models.CharField(max_length=255, blank=False, null=True,unique=True,default='',help_text='货位号')
    location_total_capacity=models.DecimalField(max_digits=12,decimal_places=4,help_text='仓号总容量')
    warehouse_total_capacity=models.DecimalField(max_digits=12, decimal_places=4, help_text='货位容量')
    find_code = models.CharField(max_length=255, blank=False, null=True,unique=True,default='',help_text='查询编码')
    py_abbreviation=models.CharField(max_length=255,blank=False,null=True,unique=False,default='',help_text='拼音简写')