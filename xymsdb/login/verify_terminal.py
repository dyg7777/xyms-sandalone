# -*- coding: utf-8 -*-
from .models import Enterprise, login_logs
from django.db.models import Q


class VerifyTerminal():
    def verify_terminal(self, uuid_code, retu_code, enter_code):
        verify_enter = Enterprise.objects.filter(
            Q(enter_code=enter_code)).count()
        if verify_enter == 0:
            return '0'
        else:
            verify_dev = login_logs.objects.filter(
                Q(login_uuid=uuid_code) & Q(return_uuid=retu_code)).count()
            if verify_dev == 0:
                return '0'
            else:
                return '1'
