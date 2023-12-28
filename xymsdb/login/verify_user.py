# -*- coding: utf-8 -*-

import json
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.db.models import Q
from .models import User_local, Enterprise
from .verify_terminal import VerifyTerminal

# 本企业用户验证信息


class VerifyUserInformation():

    # 添加新用户
    def set_user_information(request):
        data = json.loads(request.body)
        local_uuid = data['uuid']
        return_uuid = data['retuuid']
        enter_name = data['entername']
        u_name = data['user_name']
        u_password = data['password']
        u_permissions_name = data['user_permissions']
        retdata = []
        verres = VerifyTerminal.verify_terminal(
            VerifyTerminal(), local_uuid, return_uuid, enter_name)
        if verres == '0':
            res = {
                'status': 'no',
                'info': '信息验证失败,本次登录为非法尝试。',
            }
            retdata.append(res)
            jsondata = json.dumps(retdata)
            return HttpResponse(content=jsondata)
        elif verres == '1':
            try:
                res = User_local.objects.filter(
                    Q(username=u_name) & Q(enter_name=data['entername'])).count()
                if res == 0:
                    res = User_local.objects.create(username=make_password(
                        data['username'], salt='980513', hasher='default'), password=make_password(
                        data['passwd'], salt='1975217', hasher='default'), show_name=data['showname'], user_permissions='2006', enter_name='鑫奕科创')
                    retdata.append({
                        'status': 'ok',
                        'info': '用户添加成功。'
                    })
                    jsondata = json.dumps(retdata)
                    return HttpResponse(content=jsondata)
            except:
                retdata.append({
                    'status': 'no',
                    'info': '用户添加失败，请检查信息完整性或用户名已经被占中。'
                })
                jsondata = json.dumps(retdata)
                return HttpResponse(content=jsondata)

    # 修改用户信息

    def edit_user_inofrmations(request):
        pass

    # 删除用户信息

    def delete_user_inofrmations(request):
        pass

    # 设置用户时获取用户列表

    def get_user_list(request):
        pass

    def get_user_permissions(request):
        pass

    # 用户登录验证

    def verify_user_information(request):
        data = json.loads(request.body)
        retdata = []
        u_name = make_password(
            data['username'], salt='980513', hasher='default')
        u_pwd = make_password(data['passwd'], salt='1975217', hasher='default')
        verres = VerifyTerminal.verify_terminal(
            VerifyTerminal(), data['uuid'], data['retuuid'], data['entername'])

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
                verify_user = User_local.objects.filter(
                    Q(username=u_name)).count()
                if verify_user == 0:
                    res = {
                        'status': 'no',
                        'info': '无此用户。',
                    }
                    retdata.append(res)
                    jsondata = json.dumps(retdata)
                    return HttpResponse(content=jsondata)
                else:
                    verify_user = User_local.objects.filter(
                        Q(username=u_name) & Q(enter_name=data['entername'])).count()
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
                            password=u_pwd) & Q(enter_name=data['entername'])).count()
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
                                password=u_pwd) & Q(enter_name=data['entername']))
                            for value in verify_user.values():
                                res = {
                                    'status': 'OK',
                                    'info': '登录成功。',
                                    'name_cn': value.get('show_name'),
                                    'name_id': value.get('id'),
                                    'user_permiss': value.get('user_permissions')
                                }
                                retdata.append(res)
                            jsondata = json.dumps(retdata)
                            return HttpResponse(content=jsondata)
            except Exception as e:
                res = {
                    'status': 'no',
                    'info': '未能正确完成验证，本次登录为非法尝试。',
                }
                retdata.append(res)
                jsondata = json.dumps(retdata)
                return HttpResponse(content=jsondata)
