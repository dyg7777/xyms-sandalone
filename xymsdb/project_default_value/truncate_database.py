from typing import dataclass_transform

from django.http import HttpResponseRedirect
from ..grain_in.models import OwnerForGoods, QualityInspectionDeductionStandardFile, QualityInspectionDeductionStandard, QualityInspectionDeductionStandardBack, MoisturePrice, LocationWarehouseNumber, UnloadingFee, GrainSellerInformations, CarDriverAndVehicleInformations, grain_in_main
from django.db import connection


def truncate_DB(request):
    if request.method == "GET":
        return HttpResponseRedirect('欢迎访问哈尔滨市双城区鑫奕科创电脑信息服务中心数据中心')
    if request.method == "POST":
        data_str = request.POST.body()
        sql_str = 'truncate table `grain_in_cardriverandvehicleinformations`;'
        conn = connection.cursor()
        conn.execute(sql_str)
        sql_str = 'truncate table `grain_in_grain_in_main`;'
        conn = connection.cursor()
        conn.execute(sql_str)
        sql_str = 'truncate table `grain_in_grainsellerinformations`;'
        conn = connection.cursor()
        conn.execute(sql_str)
        sql_str = 'truncate table `grain_in_unloadingfee`;'
        conn = connection.cursor()
        conn.execute(sql_str)
        sql_str = 'truncate table `grain_in_locationwarehousenumber`;'
        conn = connection.cursor()
        conn.execute(sql_str)
        sql_str = 'truncate table `grain_in_ownerforgoods`;'
        conn = connection.cursor()
        conn.execute(sql_str)
        sql_str = 'truncate table `grain_in_qualityinspectiondeductionstandard`;'
        conn = connection.cursor()
        conn.execute(sql_str)
        sql_str = 'truncate table `grain_in_qualityinspectiondeductionstandardback`;'
        conn = connection.cursor()
        conn.execute(sql_str)
        conn.execute(sql_str)
        sql_str = 'truncate table `grain_in_qualityinspectiondeductionstandardfile`;'
        conn = connection.cursor()
        conn.execute(sql_str)
        sql_str = 'truncate table `grain_in_moistureprice`;'
        conn = connection.cursor()
        conn.execute(sql_str)
