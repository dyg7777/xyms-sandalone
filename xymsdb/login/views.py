# -*- coding: utf-8 -*-
from django.db.models import Q
from datetime import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
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
        dev_uuid = data['dev_uid']
        retuuid = Encrypt_code.make_encrypt_code(Encrypt_code(), localuuid)
        retsql = Enterprise.objects.all()
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
