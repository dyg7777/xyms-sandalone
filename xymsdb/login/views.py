# -*- coding: utf-8 -*-
from django.db.models import Q
from datetime import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .create_uuid import Encrypt_code
from .models import Enterprise, User_local, login_logs
from .verify_terminal import VerifyTerminal


class InitialValidation():

    # 获得企业信息

    def get_enterprise_information(request):
        data = json.loads(request.body)
        localuuid = data['local_uuid']
        dev_uuid = data['dev_uuid']
        retuuid = Encrypt_code.make_encrypt_code(Encrypt_code(), localuuid)
        retsql = Enterprise.objects.all()
        if retsql.count() > 0:
            data = []
            for ll in retsql.values():
                start_t = datetime.strftime(
                    ll.get('enter_author_start_date'), "%Y-%m-%d,%H:%M:%S")
                end_t = datetime.strftime(
                    ll.get('enter_author_end_date'), "%Y-%m-%d,%H:%M:%S")
                enter_code = ll.get('enter_code')

                res = {
                    'status': 'ok',
                    'retuuid': retuuid,
                    'enter_name': ll.get('enter_name'),
                    'enter_uncode': ll.get('enter_uncode'),
                    'enter_code': ll.get('enter_code'),
                    'enter_author_start_date': start_t,
                    'enter_author_end_date': end_t,
                    'enter_free_credit': ll.get('enter_free_credit'),
                    'version_number': ll.get('version_number'),
                    'app_name': ll.get('app_name'),
                }
                retsql = login_logs.objects.create(
                    login_uuid=localuuid, return_uuid=retuuid, login_enter_code=enter_code, login_dev_uuid=dev_uuid)
                retsql.save()
                data.append(res)
            ret_data = json.dumps(data)
            return HttpResponse(ret_data)
        elif retsql.count() == 0:
            res = {
                'status': 'no business information',
                'info': '初始用户请先注册您的企业，办结手续后再享受尊贵服务！',
            }
            data.append(res)
            ret_data = json.dumps(data)
            return HttpResponse(ret_data)

# 验证用户库是否为空

    def get_user_information(request):
        data = json.loads(request.body)
        retdata = []
        local_uuid = data['local_uuid']
        return_uuid = data['ret_uuid']
        dev_uuid = data['dev_uuid']
        lenter_code = data['enter_code']
        verres = VerifyTerminal.verify_terminal(
            VerifyTerminal(), local_uuid, return_uuid, lenter_code, dev_uuid)
        if verres == '0':
            res = {
                'status': 'no',
                'info': '信息验证失败，本次登录为非法尝试。',
            }
            retdata.append(res)
            jsondata = json.dumps(retdata)
            return HttpResponse(content=jsondata)
        elif verres == '1':
            try:
                retsql = User_local.objects.all()
                if retsql.count() == 0:
                    res = {
                        'status': 'no user information',
                        'info': '初始用户请先注册您的企业，办结手续后再享受尊贵服务！',
                    }
                    data.append(res)
                    ret_data = json.dumps(data)
                    return HttpResponse(ret_data)
                elif retsql.count() > 0:
                    res = {
                        'status': 'ok',
                        'info': '获得用户信息成功！',
                    }
                    data.append(res)
                    ret_data = json.dumps(data)
                    return HttpResponse(ret_data)
            except Exception as e:
                res = {
                    'status': 'no',
                    'info': '信息验证失败！',
                }
                data.append(res)
                ret_data = json.dumps(data)
                return HttpResponse(ret_data)
