from re import T
from django.db import models
import uuid
from django.utils.timezone import timezone
from pymysql import NULL
from .. login.models import Enterprise
# Create your models here.


# 货权人信息
class OwnerForGoods(models.Model):
    ownerforgoods_name=models.CharField(max_length=120,blank=False,null=False,unique=True,default='企业私有',help_text='货权人名称')
    ownerforgoods_uncode=models.CharField(max_length=100,blank=False,null=False,default='',help_text='货权人代码')
    ownerforgoods_phonenumber=models.CharField(max_length=100,blank=True,null=True,default='',help_text='货权人联系方式')
    co_owners=models.CharField(max_length=120,blank=True,null=True,default='',help_text='货物共有人')


# 收购品种
class AcquisitionVarieties(models.Model):
    AV_name=models.CharField(max_length=50, blank=False, null=False,unique=True,default='玉米',help_text='收购品种')
    find_code = models.CharField(max_length=20, blank=True, null=True,unique=True,default='',help_text='查询编码')
    py_abbreviation=models.CharField(max_length=20,blank=True,null=True,unique=False,default='',help_text='拼音简写')
    acquisitioncaps = models.DecimalField(max_digits=12 ,decimal_places=4,help_text='收购上限')


# 玉米收购国标
class GBCornInformations(models.Model):
    acquisitionVarietiesid=models.ForeignKey(AcquisitionVarieties,related_name='acquisition_varities',on_delete=models.CASCADE,help_text='收购品种库ID')
    GB_filename = models.CharField(max_length=50, blank=False, null=False,help_text='国标文件号')
    GB_file_contents=models.TextField(blank=True,null=True,default='',help_text='文件内容')
    purchase_price=models.DecimalField(max_digits=12,decimal_places=6,help_text='等级价格')
    purchase_name = models.CharField(max_length=20, blank=False, null=False,unique=True,default="",help_text='等级名称')
    test_weight_high=models.DecimalField(max_digits=6, blank=True,null=True,decimal_places=1, help_text="容重上限3.1")
    test_weight_low=models.DecimalField(max_digits=6,blank=True,null=True, decimal_places=1, help_text="容重下限3.1")
    defective_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='不完善粒标准3.2')
    insect_damaged_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='虫蚀粒标准3.2.1')
    spotted_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='病斑粒标准3.2.2')
    broken_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='破损粒标准3.2.3')
    sprouted_kernels = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True,help_text='生芽粒标准3.2.4')
    moldy_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='生霉粒标准3.2.5')
    heat_damaged_kernels = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True, help_text='热损伤粒标准3.2.6')
    nature_heat_damaged_kernels = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True,help_text='自然热损伤粒标准3.2.6.1')
    drying_heat_damaged_kernels=models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True,help_text='烘干热损伤粒标准3.2.6.2')
    foreign_matter=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='杂质标准3.3')
    throughs = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True, help_text='筛下物标准3.3.1')
    inorganic_impurities=models.DecimalField(max_digits=6,blank=True,null=True, decimal_places=1, help_text='无机杂质3.3.2')
    organic_impurities = models.DecimalField(max_digits=6,blank=True,null=True, decimal_places=1, help_text='有机杂质3.3.3')
    colour=models.CharField(max_length=10,default='正常',blank=True,null=True,help_text='色泽3.4')
    odour=models.CharField(max_length=10, default="正常",blank=True,null=True, help_text='气味3.5')
    moisture_content=models.DecimalField(max_digits=6,blank=True,null=True,decimal_places=1,help_text='水份标准3.6')
    severely_moldy_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='霉变粒标准3.7')
    eidt_datetime=models.DateTimeField(auto_now_add=True,help_text='创建时间')
    create_datetime = models.DateTimeField(auto_now=True,help_text='最后修改时间')
   
# 质检扣量标准
    # 文件
class QualityInspectionDeductionStandardFile(models.Model):
    file_number=models.CharField(max_length=50,blank=True,null=True,default='',help_text='文件号')
    file_contents=models.TextField(default='',help_text='文件内容')
    create_datetime=models.DateTimeField(auto_now_add=True,help_text='创建时间')
    edit_datetime = models.DateTimeField(auto_now=True,help_text='最后修改时间')
    status=models.CharField(max_length=2,blank=True,null=True,default='1',help_text='记录状态0失效')
    # 扣量标准
class QualityInspectionDeductionStandard(models.Model): 
    file_id=models.ForeignKey(QualityInspectionDeductionStandardFile,on_delete=models.CASCADE,help_text='对应质检文件ID号')
    field_name=models.CharField(max_length=100,blank=True,null=True,default='',help_text='对应字段名')
    chinese_annotation=models.CharField(max_length=100,blank=True,null=True,default='',help_text='中文标注')
    range_upper_limit=models.DecimalField(max_digits=10,decimal_places=2,help_text='范围上限')
    range_lower_limit=models.DecimalField(max_digits=10,decimal_places=2,help_text='范围下限')
    operator_upper_limit=models.CharField(max_length=10,blank=True,null=True,default='',help_text='上限数学运算符')
    operator_lower_limit=models.CharField(max_length=10,blank=True,null=True,default='',help_text='下限数学运算符')
    deduction_ratio=models.DecimalField(max_digits=10,decimal_places=2,help_text='扣减比例')
    increment_scale=models.DecimalField(max_digits=10,decimal_places=2,help_text='增量比例')
    create_datetime=models.DateTimeField(auto_now_add=True,help_text='创建时间')
    edit_datetime = models.DateTimeField(auto_now=True,help_text='最后修改时间')
    status=models.CharField(max_length=2,blank=True,null=True,default='1',help_text='记录状态0失效')
        #质检标准操作备份
class QualityInspectionDeductionStandardBack(models.Model):
    operation_type=models.CharField(max_length=50,blank=True,null=True,default='',help_text='操作类型，例如删除、修改')
    file_eidt_datetime=models.DateTimeField(auto_now_add=True,help_text='创建时间') 
    file_number=models.CharField(max_length=50,blank=True,null=True,default='',help_text='文件号')
    file_contents=models.TextField(default='',help_text='文件内容')
    file_create_datetime=models.DateTimeField(auto_now_add=True,help_text='创建时间')
    file_edit_datetime = models.DateTimeField(auto_now=True,help_text='最后修改时间')
    field_name=models.CharField(max_length=100,blank=True,null=True,default='',help_text='对应字段名')
    chinese_annotation=models.CharField(max_length=100,blank=True,null=True,default='',help_text='中文标注')
    range_upper_limit=models.DecimalField(max_digits=10,decimal_places=2,help_text='范围上限')
    range_lower_limit=models.DecimalField(max_digits=10,decimal_places=2,help_text='范围下限')
    operator_upper_limit=models.CharField(max_length=10,blank=True,null=True,default='',help_text='上限数学运算符')
    operator_lower_limit=models.CharField(max_length=10,blank=True,null=True,default='',help_text='下限数学运算符')
    deduction_ratio=models.DecimalField(max_digits=10,decimal_places=2,help_text='扣减比例')
    increment_scale=models.DecimalField(max_digits=10,decimal_places=2,help_text='增量比例')
    index_create_datetime=models.DateTimeField(auto_now_add=True,help_text='创建时间')
    index_edit_datetime = models.DateTimeField(auto_now=True,help_text='最后修改时间')

# 水份定价表
class MoisturePrice(models.Model):
    varieties_id=models.ForeignKey(AcquisitionVarieties,blank=True,null=True,on_delete=models.CASCADE,help_text='品种ID')
    purchase_id=models.ForeignKey(GBCornInformations,blank=True,null=True,on_delete=models.DO_NOTHING,help_text='等级标准')
    moisture=models.DecimalField(max_digits=7, blank=True,null=True,decimal_places=4, help_text="水份值")
    price=models.DecimalField(max_digits=7, decimal_places=4,blank=True,null=True, help_text="水份对应价格")


# 包装物设置
class Packaging(models.Model):
    packag_name = models.CharField(max_length=30, blank=True,null=True,default='散积',unique=True,help_text='包装物名称')
    find_code = models.CharField(max_length=20, blank=True, null=True,unique=True,default='',help_text='查询编码')
    py_abbreviation=models.CharField(max_length=20,blank=False,null=False,unique=False,default='',help_text='拼音简写')


# 车种设置
class VehicleType(models.Model):
    vehicle_type=models.CharField(max_length=30, blank=True, null=True,unique=True,default='',help_text='车辆类型')
    find_code = models.CharField(max_length=20, blank=True, null=True,unique=True,default='',help_text='查询编码')
    py_abbreviation=models.CharField(max_length=20,blank=False,null=False,unique=False,default='',help_text='拼音简写')


# 货位仓号
class LocationWarehouseNumber(models.Model):
    location_number = models.CharField(max_length=30, blank=True, null=True,unique=True,default='',help_text='仓号')
    warehouse_number=models.CharField(max_length=30, blank=True, null=True,unique=True,default='',help_text='货位号')
    location_total_capacity=models.DecimalField(max_digits=12,decimal_places=4,help_text='仓号总容量')
    warehouse_total_capacity=models.DecimalField(max_digits=12, decimal_places=4, help_text='货位容量')
    find_code = models.CharField(max_length=20, blank=True, null=True,unique=True,default='',help_text='查询编码')
    py_abbreviation=models.CharField(max_length=20,blank=False,null=False,unique=False,default='',help_text='拼音简写')


# 卸车费设置
class UnloadingFee(models.Model):
    varieties_id=models.ForeignKey(AcquisitionVarieties,on_delete=models.CASCADE,help_text='品种ID')
    unloadingfee_price=models.DecimalField(max_digits=12,decimal_places=4,help_text='卸车费按公斤计算')

# 售粮人信息

class GrainSellerInformations(models.Model):
    grainseller_name=models.CharField(max_length=60,blank=False,null=False,default='',help_text='售粮人姓名')
    grainseller_uncode=models.CharField(max_length=20, blank=True, null=True,default='',help_text='身份证号')
    grainseller_uncode_photo=models.TextField( blank=True, null=True,default='',help_text='售粮人身份证照片')
    grainseller_photo=models.TextField( blank=True, null=True,default='',help_text='售粮人本人照片')
    grainseller_sex = models.CharField(max_length=10, blank=True, null=True,default='',help_text='售粮人性别')
    grainseller_ethnic=models.CharField(max_length=100, blank=True, null=True,default='',help_text='民族')
    grainseller_birthday=models.CharField(max_length=20, blank=True, null=True,default='',help_text='出生年月')
    grainseller_address=models.CharField(max_length=120, blank=True, null=True,default='',help_text='身份证地址')
    grainseller_issuing_authority=models.CharField(max_length=120, blank=True, null=True,default='',help_text='发证机关')
    grainseller_expiration_date=models.CharField(max_length=30, blank=True, null=True,default='',help_text='证件有效期')
    grainseller_phone=models.CharField(max_length=20, blank=True, null=True,default='',help_text='联系电话')
    grainseller_photo_in_uncode=models.TextField( blank=True, null=True,default='',help_text='售粮人身份证内照片')
    grainseller_bank_name=models.CharField(max_length=120, blank=True, null=True,default='',help_text='开户银行名称')
    grainseller_bank_card_number=models.CharField(max_length=30, blank=True, null=True,default='',help_text='银行卡号')
    grainseller_bank_account=models.CharField(max_length=50, blank=True, null=True,default='',help_text='银行账号')

# 车辆省份信息
class VehicleProvince(models.Model):
    province_id=models.CharField(max_length=20,unique=True,blank=True,null=True,default='',help_text='省份代码')
    province_name=models.CharField(max_length=120,unique=True,blank=False,null=False,default='',help_text='省份名称')
    province_code=models.CharField(max_length=10,unique=True,blank=False,null=False,default='',help_text='省份简称')
    city_id=models.CharField(max_length=20,unique=True,blank=True,null=True,default='',help_text='城市代码')
    city_name=models.CharField(max_length=120,unique=True,blank=False,null=False,default='',help_text='城市名称')
    city_code=models.CharField(max_length=10,unique=True,blank=False,null=False,default='',help_text='城市简称')



# 司机车辆信息
class CarDriverAndVehicleInformations(models.Model):
    driver_name = models.CharField(max_length=80, blank=True,null=True,default='',help_text='司机姓名')
    driver_uncode = models.CharField(max_length=80, blank=True,null=True,default='',help_text='司机身份证号')
    driver_uncode_photo = models.TextField(blank=True,null=True,default='',help_text='司机身份证照片')
    driver_photo = models.TextField(blank=True,null=True,default='',help_text='司机照片')
    vehicle_province=models.CharField(max_length=20, blank=True,null=True,default='',help_text='牌照号')

    
# 主数据库
class grain_in_main(models.Model):
    
    # 收购信息
    main_guid=models.CharField(max_length=60, blank=False, null=False,unique=True,default=uuid.uuid4().hex,help_text='记录的UID')
    create_time = models.DateTimeField(auto_now_add=True,help_text='记录创建时间')
    grain_type = models.CharField(max_length=50,blank=True,null=True,help_text='粮食类型')
    acquisition_type= models.CharField(max_length=50,blank=True,null=True,help_text='收购类型')
    test_sheets_number= models.CharField(max_length=50,blank=True,null=True,help_text='化验单号')
    upload_code=models.CharField(max_length=50, blank=True, null=True,help_text='传输编号')
    # 售粮人信息
    grainseller_name=models.CharField(max_length=60,blank=False,null=False,default='',help_text='售粮人姓名')
    grainseller_uncode=models.CharField(max_length=20, blank=True, null=True,default='',help_text='身份证号')
    grainseller_uncode_photo=models.TextField( blank=True, null=True,default='',help_text='售粮人身份证照片')
    grainseller_photo=models.TextField( blank=True, null=True,default='',help_text='售粮人本人照片')
    grainseller_sex = models.CharField(max_length=10, blank=True, null=True,default='',help_text='售粮人性别')
    grainseller_ethnic=models.CharField(max_length=100, blank=True, null=True,default='',help_text='民族')
    grainseller_birthday=models.CharField(max_length=20, blank=True, null=True,default='',help_text='出生年月')
    grainseller_address=models.CharField(max_length=120, blank=True, null=True,default='',help_text='身份证地址')
    grainseller_issuing_authority=models.CharField(max_length=120, blank=True, null=True,default='',help_text='发证机关')
    grainseller_expiration_date=models.CharField(max_length=30, blank=True, null=True,default='',help_text='证件有效期')
    grainseller_phone=models.CharField(max_length=20, blank=True, null=True,default='',help_text='联系电话')
    grainseller_photo_in_uncode=models.TextField( blank=True, null=True,default='',help_text='售粮人身份证内照片')
    grainseller_bank_name=models.CharField(max_length=120, blank=True, null=True,default='',help_text='开户银行名称')
    grainseller_bank_card_number=models.CharField(max_length=30, blank=True, null=True,default='',help_text='银行卡号')
    grainseller_bank_account=models.CharField(max_length=50, blank=True, null=True,default='',help_text='银行账号')
    # 司机、车辆、仓位和包装物信息
    driver_name = models.CharField(max_length=80, blank=True,null=True,default='',help_text='司机姓名')
    driver_uncode = models.CharField(max_length=80, blank=True,null=True,default='',help_text='司机身份证号')
    driver_uncode_photo = models.TextField(blank=True,null=True,default='',help_text='司机身份证照片')
    driver_photo = models.TextField(blank=True,null=True,default='',help_text='司机照片')
    vehicle_type=models.CharField(max_length=30, blank=True, null=True,unique=True,default='',help_text='车辆类型')
    vehicle_province=models.CharField(max_length=20, blank=True,null=True,default='',help_text='车辆牌照号')
    grainseller_driver=models.CharField(max_length=6, blank=True,null=True,default='是',help_text='售粮人和司机是否同一人')
    packag_name = models.CharField(max_length=30, blank=True,null=True,default='散积',unique=True,help_text='包装物名称')
    location_number = models.CharField(max_length=30, blank=True, null=True,unique=True,default='',help_text='仓号')
    warehouse_number=models.CharField(max_length=30, blank=True, null=True,unique=True,default='',help_text='货位号')
    total_vehicle_front_photo=models.TextField(blank=True,null=True,default='',help_text='毛重过磅车辆正面照片')
    total_vehicle_rear_photo=models.TextField(blank=True,null=True,default='',help_text='毛重过磅车尾照片')
    empty_vehicle_front_photo=models.TextField(blank=True,null=True,default='',help_text='皮重过磅车辆正面照片')
    empty_vehicle_rear_photo=models.TextField(blank=True,null=True,default='',help_text='皮重过磅车尾照片')
    # 货权人
    ownerforgoods_name=models.CharField(max_length=120,blank=False,null=False,unique=True,default='企业私有',help_text='货权人名称')
    ownerforgoods_uncode=models.CharField(max_length=100,blank=False,null=False,default='',help_text='货权人代码')
    ownerforgoods_phonenumber=models.CharField(max_length=100,blank=True,null=True,default='',help_text='货权人联系方式')
    co_owners=models.CharField(max_length=120,blank=True,null=True,default='',help_text='货物共有人')
    # 收购企业
    enterprise_id=models.ForeignKey(Enterprise,on_delete=models.CASCADE,help_text='收购企业ID')
    # 质检、卸车费标准信息
    AV_name=models.CharField(max_length=50, blank=False, null=False,unique=True,default='玉米',help_text='收购品种')
    purchase_price=models.DecimalField(max_digits=12,decimal_places=6,help_text='等级价格')
    purchase_name = models.CharField(max_length=20, blank=False, null=False,unique=True,default="",help_text='等级名称')
    test_weight_high=models.DecimalField(max_digits=6, blank=True,null=True,decimal_places=1, help_text="容重上限3.1")
    test_weight_low=models.DecimalField(max_digits=6,blank=True,null=True, decimal_places=1, help_text="容重下限3.1")
    defective_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='不完善粒标准3.2')
    insect_damaged_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='虫蚀粒标准3.2.1')
    spotted_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='病斑粒标准3.2.2')
    broken_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='破损粒标准3.2.3')
    sprouted_kernels = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True,help_text='生芽粒标准3.2.4')
    moldy_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='生霉粒标准3.2.5')
    heat_damaged_kernels = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True, help_text='热损伤粒标准3.2.6')
    nature_heat_damaged_kernels = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True,help_text='自然热损伤粒标准3.2.6.1')
    drying_heat_damaged_kernels=models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True,help_text='烘干热损伤粒标准3.2.6.2')
    foreign_matter=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='杂质标准3.3')
    throughs = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True, help_text='筛下物标准3.3.1')
    inorganic_impurities=models.DecimalField(max_digits=6,blank=True,null=True, decimal_places=1, help_text='无机杂质3.3.2')
    organic_impurities = models.DecimalField(max_digits=6,blank=True,null=True, decimal_places=1, help_text='有机杂质3.3.3')
    colour=models.CharField(max_length=10,default='正常',blank=True,null=True,help_text='色泽3.4')
    odour=models.CharField(max_length=10, default="正常",blank=True,null=True, help_text='气味3.5')
    moisture_content=models.DecimalField(max_digits=6,blank=True,null=True,decimal_places=1,help_text='水份标准3.6')
    severely_moldy_kernels=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='霉变粒标准3.7')
    unloadingfee_price=models.DecimalField(max_digits=12,decimal_places=4,help_text='卸车费按公斤计算')
        # 质检数据实时数值
    truevalue_test_weight=models.DecimalField(max_digits=6,blank=True,null=True, decimal_places=1, help_text="容重")
    truevalue_defective=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='不完善粒')
    truevalue_insect_damaged=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='虫蚀粒')
    truevalue_spotted=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='病斑粒')
    truevalue_broken=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='破损粒')
    truevalue_sprouted = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True,help_text='生芽粒')
    truevalue_moldy=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='生霉粒')
    truevalue_heat_damaged = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True, help_text='热损伤粒')
    truevalue_nature_heat_damaged = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True,help_text='自然热损伤粒')
    truevalue_drying_heat_damaged=models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True,help_text='烘干热损伤粒')
    truevalue_foreign_matter=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='杂质')
    truevalue_throughs = models.DecimalField(max_digits=6, decimal_places=1,blank=True,null=True, help_text='筛下物')
    truevalue_inorganic_impurities=models.DecimalField(max_digits=6,blank=True,null=True, decimal_places=1, help_text='无机杂质')
    truevalue_organic_impurities = models.DecimalField(max_digits=6,blank=True,null=True, decimal_places=1, help_text='有机杂质')
    truevalue_colour=models.CharField(max_length=10,default='正常',blank=True,null=True,help_text='色泽')
    truevalue_odour=models.CharField(max_length=10, default="正常",blank=True,null=True, help_text='气味')
    truevalue_moisture_content=models.DecimalField(max_digits=6,blank=True,null=True,decimal_places=1,help_text='水份')
    truevalue_severely_moldy=models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True,help_text='霉变粒')
    # 重量信息
    total_weight=models.DecimalField(max_digits=12,decimal_places=0,help_text='毛重')
    empty_weight=models.DecimalField(max_digits=12,decimal_places=0,help_text='皮重')
    total_subtract_empty_weight=models.DecimalField(max_digits=12,decimal_places=0,help_text='毛减皮重量')
    Weight_deduction_on_site=models.DecimalField(max_digits=12,decimal_places=0,help_text='现场掺杂扣减重量')
    net_weight=models.DecimalField(max_digits=12,decimal_places=0,help_text='净重量')
    defective_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='不完善粒扣减重量')
    insect_damaged_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='虫蚀粒扣减重量')
    spotted_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='病斑粒扣减重量')
    broken_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='破损粒扣减重量')
    sprouted_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='生芽粒扣减重量')
    moldy_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='生霉粒扣减重量')
    heat_damaged_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='热损伤粒扣减重量')
    nature_heat_damaged_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='自然热损伤粒扣减重量')
    drying_heat_damaged_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='烘干热损伤粒扣减重量')
    foreign_matter_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='杂质扣减重量')
    throughs_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='筛下物扣减重量')
    inorganic_impurities_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='无机杂质扣减重量')
    organic_impurities_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='有机杂质扣减重量')
    moisture_content_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='水份扣减重量')
    severely_moldy_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='霉变粒扣减重量')
    deducted_weight=models.DecimalField(max_digits=8,decimal_places=4,help_text='定扣重比例')
    uantitative_weight_deducted=models.DecimalField(max_digits=12,decimal_places=0,help_text='定比例扣减重量')
    pure_weight=models.DecimalField(max_digits=12,decimal_places=0,help_text='纯重')
    # 单价
    unit_price=models.DecimalField(max_digits=12,decimal_places=5,help_text='商品单价')
    accounts_payable=models.DecimalField(max_digits=15,decimal_places=2,help_text='应付金额')
    deduction_unloadingfee_amount=models.DecimalField(max_digits=15,decimal_places=2,help_text='扣卸车费')
    actual_payment=models.DecimalField(max_digits=15,decimal_places=2,help_text='实付金额')
    # 各种时间
    check_in_datetime=models.DateTimeField(default=timezone.now,help_text='登记时间')
    total_weight_datetime=models.DateTimeField(help_text='毛重过磅时间')
    empty_weight_datetime=models.DateTimeField(help_text='皮重过磅时间')
    print_ticket_datetime=models.DateTimeField(help_text=' 结算打票时间')
    payment_datetime=models.DateTimeField(help_text='付款时间')
    upload_datetime=models.DateTimeField(help_text='上传时间')
    # 各种状态
    check_in_status=models.CharField(max_length=1,blank=True,null=True,help_text='完成登记')
    total_weight_status=models.CharField(max_length=1,blank=True,null=True,help_text='完成毛重过磅')
    empty_weight_status=models.CharField(max_length=1,blank=True,null=True,help_text=' 完成皮重过磅')
    print_ticket_status=models.CharField(max_length=1,blank=True,null=True,help_text=' 完成打票')
    payment_status=models.CharField(max_length=1,blank=True,null=True,help_text=' 完成付款')
    upload_status=models.CharField(max_length=1,blank=True,null=True,help_text=' 完成上传')
    # 人员
    chemist_name=models.CharField(max_length=50,blank=True,null=True,help_text='化验员')
    test_data_entry_name=models.CharField(max_length=50,blank=True,null=True,help_text='化验录入员')
    total_weight_persions_name=models.CharField(max_length=50,blank=True,null=True,help_text='毛重检斤员')
    empty_weight_persions_name=models.CharField(max_length=50,blank=True,null=True,help_text='皮重检斤员')
    weight_persions_name=models.CharField(max_length=50,blank=True,null=True,help_text='统一检斤员')
    print_ticket_persion_name=models.CharField(max_length=50,blank=True,null=True,help_text='付款打票员')
    cash_management_persion_name=models.CharField(max_length=50,blank=True,null=True,help_text='现金')
    accounting_persion_name=models.CharField(max_length=50,blank=True,null=True,help_text='会计')
    payment_persion_name=models.CharField(max_length=50,blank=True,null=True,help_text='付款员')
    
