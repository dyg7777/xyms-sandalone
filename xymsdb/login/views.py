from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .set_default import *


class ResetDefault():
    def set_login_default(requests):
        rundate_default()
        userpermissions_default()
        user_default()
        return HttpResponse('ok')
