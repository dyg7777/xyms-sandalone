from datetime import date
from http.client import responses
import pprint
import json
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .set_default import *
from pprint import pprint
import requests
from .create_uuid import Encrypt_code
from .models import Enterprise, login_logs


class ResetDefault():

    def set_login_default(request):
        data = json.loads(request.body)
        pprint(data['name'])
        pprint(type(data['name']))

        data1 = [{"aaa": 232342, '我是测试': '对，你是23423测试'}, {"aaa": 23, '我是测试': '对，你是测试'},
                 {"aaa1": 213, '我是测试1': '对2，你是测试'}]
        json_data = json.dumps(data1)

        # rundate_default()
        # userpermissions_default()
        # user_default()
        return HttpResponse(json_data)

    # 获得企业信息
    def get_enterprise_information(request):
        data = json.loads(request.body)
        localuuid = data['uuid']
        retuuid = Encrypt_code.make_encrypt_code(Encrypt_code(), localuuid)
        retsql = login_logs.objects.create(
            login_uuid=localuuid, return_uuid=retuuid)
        retsql.save()
        retsql = Enterprise.objects.all()
        data = []
        for ll in retsql.values():
            res = {
                'enter_name': ll.get('enter_name'),

            }
            data.append(res)
        ret_data = json.dumps(data)
        return HttpResponse(content=ret_data, content_type='applicaton/json')
