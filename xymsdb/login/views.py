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
