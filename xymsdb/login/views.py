from http.client import responses
import pprint
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .set_default import *
from pprint import pprint
import requests
class ResetDefault():
    def set_login_default(request):
        pprint(response.request.headers)

        # rundate_default()
        # userpermissions_default()
        # user_default()
        return HttpResponse('ok')
