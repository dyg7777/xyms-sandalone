from email import charset
from django.http import HttpResponse
import http.client
import time
from datetime import datetime
from .models import RunDate, UserPermissions, User_local, ProgectPath, DatabasePath
from django.db import connection
from django.utils import timezone
# 初始化系统时间


def rundate_default():
    sql_str = 'truncate table `login_rundate`;'
    conn = connection.cursor()
    conn.execute(sql_str)
    conn.close()
    connection.close()
    conn1 = http.client.HTTPConnection('www.xy2cn.com')
    conn1.request("GET", "/")
    rsp = conn1.getresponse()
    timestamp = rsp.getheader('date')
    ltime = time.strptime(timestamp[5:25], "%d %b %Y %H:%M:%S")
    bjtime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
    date = "%u-%02u-%02u" % (bjtime.tm_year, bjtime.tm_mon, bjtime.tm_mday)
    tm = "%02u:%02u:%02u" % (bjtime.tm_hour, bjtime.tm_min, bjtime.tm_sec)
    dt = date+" "+tm
    retu = RunDate.objects.create(
        run_datetime=datetime.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return HttpResponse(retu)


# 用户权限

def userpermissions_default():
    DEFAULT=(
        (1000, '粮质化验检验岗'),
        (1001, '化验检验数据录入岗'),
        (1002, '化验检验数据统计岗'),
        (2001, '入库空车称重过磅岗'),
        (2002, '入库重车称重过磅岗'),
        (2003, '单磅入库称重过磅岗'),
        (2004, '出库重车称重过磅岗'),
        (2005, '出库空车称重过磅岗'),
        (2006, '单磅出库称重过磅岗'),
        (2007, '过磅数据统计岗'),
        (3000, '付款出票操作岗'),
        (3001, '付款票据核对岗'),
        (3002, '付款现金支付岗'),
        (3003, '付款现金复核岗'),
        (3004, '付款数据统计岗'),
        (3005, '会计岗'),
        (4000, '出库数据统计岗'),
        (5000, '仓储岗'),
        (6000, '高层核心人员访问岗'),
        (7000, '数据管理人员岗'),
        (8000, '参数设置管理岗'),
        (9000, '最高权限管理岗'),
        (0000,'初始状态'),
    )
    sql_str = 'truncate table `login_userpermissions`;'
    conn = connection.cursor()
    conn.execute(sql_str)
    conn.close()
    connection.close()
    for ll in DEFAULT:
        retu=UserPermissions.objects.create(permissions_code=str(ll[0]),permissions_name=ll[1])
        retu.save()

# 用户库初始化

def user_default():
    sql_str = 'truncate table `login_user_local`;'
    conn = connection.cursor()
    conn.execute(sql_str)
    conn.close()
    connection.close()
    retu=User_local.objects.create(user_permissions='0000')
    retu.save()

# 数据库配置

# 用户库初始化

def database_default():
    sql_str = 'truncate table `login_databasepath`;'
    conn = connection.cursor()
    conn.execute(sql_str)
    conn.close()
    connection.close()
    retu=User_local.objects.create(charset='utf-8')
    retu.save()