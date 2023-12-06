import json
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.db.models import Q
from .models import User_local
from .verify_terminal import VerifyTerminal


class VerifyUserInformation():
    def set_user_information(request):
        data = json.loads(request.body)

        res = User_local.objects.create(username=make_password(
            data['username'], salt='980513', hasher='default'), password=make_password(
            data['passwd'], salt='980513', hasher='default'), show_name=data['showname'], user_permissions='2006', enter_name='鑫奕科创')
        return HttpResponse(res)

    def verify_user_information(request):
        data = json.loads(request.body)
        retdata = []
        u_name = make_password(
            data['username'], salt='980513', hasher='default')
        u_pwd = make_password(data['passwd'], salt='980513', hasher='default')
        verres = VerifyTerminal.verify_terminal(
            VerifyTerminal(), data['uuid'], data['retuuid'], data['entercode'])

        if verres == '0':
            res = {
                'status': 'no',
                'info': '信息验证失败。',
            }
            retdata.append(res)
            jsondata = json.dumps(retdata)
            return HttpResponse(content=jsondata)
        elif verres == '1':
            print(9999)
            verify_user = User_local.objects.filter(Q(username=u_name)).count()
            if verify_user == 0:
                res = {
                    'status': 'no',
                    'info': '无此用户。',
                }
                retdata.append(res)
                jsondata = json.dumps(retdata)
                return HttpResponse(content=jsondata)
            else:
                print(11111)
                verify_user = User_local.objects.filter(
                    Q(username=u_name) & Q(enter_name=data['entercode'])).count()
                if verify_user == 0:
                    res = {
                        'status': 'no',
                        'info': '此用户无法登录当前企业。',
                    }
                    retdata.append(res)
                    jsondata = json.dumps(retdata)
                    return HttpResponse(content=jsondata)
                else:
                    print(0000)
                    verify_user = User_local.objects.filter(Q(username=u_name) & Q(
                        password=u_pwd) & Q(enter_name=data['entercode'])).count()
                    if verify_user == 0:
                        res = {
                            'status': 'no',
                            'info': '密码错误。',
                        }
                        retdata.append(res)
                        jsondata = json.dumps(retdata)
                        return HttpResponse(content=jsondata)
                    else:
                        verify_user = User_local.objects.filter(Q(username=u_name) & Q(
                            password=u_pwd) & Q(enter_name=data['entercode']))
                        # for value in verify_user.values():
                        res = {
                            'status': 'OK',
                            'info': '登录成功。',
                            # 'name_cn': value.get('show_name'),
                            # 'name_id': value.get('id'),
                        }
                        retdata.append(res)
                        jsondata = json.dumps(retdata)
                        return HttpResponse(content=jsondata)
