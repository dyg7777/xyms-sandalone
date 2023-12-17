from django.shortcuts import render
from django.http import HttpResponse
from .set_default import vehicle_default, acquisition_defaule, GBforCorn, vehicletypedefault, packagindefault,userpermissions_default
# Create your views here.

def default_set(requests):
# 省份+简写
    vehicle_default()
# 车辆类型
    vehicletypedefault()
# 包装信息
    packagindefault()
# 收购品种    
    acquisition_defaule()
# 国标设置
    GBforCorn()
# 用户权限
    userpermissions_default()
    return HttpResponse('ok')
