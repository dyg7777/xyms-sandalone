from datetime import date
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
import json
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .set_default import *
from pprint import pprint
from .create_uuid import Encrypt_code
from .models import Enterprise, login_logs


class ResetDefault():

    def set_enterprise_information(request):
        data = json.loads(request.body)
        return HttpResponse('ok')

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
                'status': 'ok',
                'retuuid': retuuid,
                'enter_name': ll.get('enter_name'),
                'enter_uncode': ll.get('enter_uncode'),
                'enter_code': ll.get('enter_code'),
                'enter_author_start_date': datetime.strftime(ll.get('enter_author_start_date'), "%Y-%m-%d,%H:%M:%S"),
                'enter_author_end_date': datetime.strftime(ll.get('enter_author_end_date'), "%Y-%m-%d,%H:%M:%S"),
                'enter_free_credit': ll.get('enter_free_credit'),
                'version_number': ll.get('version_number'),
                'app_name': ll.get('app_name'),
            }
            data.append(res)
        ret_data = json.dumps(data)
        return HttpResponse(content=ret_data)


class VerifyInformation():
    def get_user(request):
        data = json.loads(request.body)
        res = User_local.objects.create(username=make_password(
            data['username'], salt='980513', hasher='default'), password=make_password(
            data['passwd'], salt='980513', hasher='default'), show_name=data['showname'], user_permissions='2006', enter_name='鑫奕科创')
        return HttpResponse(res)

    def verify_user(request):
        data = json.loads(request.body)
        verify_enter = Enterprise.objects.filter(
            Q(enter_code=data.get('entercode'))).count()
        retdata = []
        if verify_enter == 0:
            res = {
                'status': 'no',
                'info': '企业信息验证失败。',
            }
            retdata.append(res)
            jsondata = json.dumps(retdata)
            return HttpResponse(content=jsondata)
        else:
            verify_dev = login_logs.objects.filter(
                Q(login_uuid=data['uuid']) & Q(return_uuid=data['retuuid'])).count()
            retdata = []
            if verify_dev == 0:
                res = {
                    'status': 'no',
                    'info': '设备验证失败。',
                }
                retdata.append(res)
                jsondata = json.dumps(retdata)
                return HttpResponse(content=jsondata)
            else:
                verify_user = User_local.objects.filter(Q(username=make_password(
                    data['username'], salt='980513', hasher='default'))).count()
                if verify_user == 0:
                    res = {
                        'status': 'no',
                        'info': '无此用户。',
                    }
                    retdata.append(res)
                    jsondata = json.dumps(retdata)
                    return HttpResponse(content=jsondata)
                else:
                    verify_user = User_local.objects.filter(Q(username=make_password(
                        data['username'], salt='980513', hasher='default')) & Q(enter_name=data['entercode'])).count()
                    if verify_user == 0:
                        res = {
                            'status': 'no',
                            'info': '此用户无法登录当前企业。',
                        }
                        retdata.append(res)
                        jsondata = json.dumps(retdata)
                        return HttpResponse(content=jsondata)
                    else:
                        verify_user = User_local.objects.filter(Q(username=make_password(
                            data['username'], salt='980513', hasher='default')) & Q(password=make_password(
                                data['passwd'], salt='980513', hasher='default'))).count()
                        if verify_user == 0:
                            res = {
                                'status': 'no',
                                'info': '密码错误。',
                            }
                            retdata.append(res)
                            jsondata = json.dumps(retdata)
                            return HttpResponse(content=jsondata)
                        else:
                            verify_user = User_local.objects.filter(Q(username=make_password(
                                data['username'], salt='980513', hasher='default')) & Q(password=make_password(
                                    data['passwd'], salt='980513', hasher='default')))
                            for value in verify_user.values():
                                res = {
                                    'status': 'OK',
                                    'info': '登录成功。',
                                    'name_cn': value.get('show_name'),
                                    'name_id': value.get('id'),
                                }
                                retdata.append(res)
                                jsondata = json.dumps(retdata)
                                return HttpResponse(content=jsondata)
