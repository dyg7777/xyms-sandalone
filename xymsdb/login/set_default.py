from django.http import HttpResponse
import http.client
import time
from datetime import datetime
from .models import RunDate, UserPermissions, User, ProgectPath, DatabasePath
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
