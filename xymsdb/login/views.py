from datetime import date
from http.client import responses
import pprint
from datetime import datetime
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
        data1 = []
        data = []
        for ll in retsql.values():
            res = {
                'enter_name': ll.get('enter_name'),
                'enter_uncode': ll.get('enter_uncode'),
                'enter_author_start_date': datetime.strftime(ll.get('enter_author_start_date'), "%Y-%m-%d,%H:%M:%S"),
                'enter_author_end_date': datetime.strftime(ll.get('enter_author_end_date'), "%Y-%m-%d,%H:%M:%S"),
                'enter_free_credit': ll.get('enter_free_credit'),
                'version_number': ll.get('version_number'),
                'app_name': ll.get('app_name'),
            }
            data.append(res)
        ret_data = json.dumps(data)
        return HttpResponse(content=ret_data, content_type='applicaton/json')
