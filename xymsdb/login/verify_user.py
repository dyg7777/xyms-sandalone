# -*- coding: utf-8 -*-

import json
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.db.models import Q
from .models import User_local, UserPermissions, login_logs
from .verify_terminal import VerifyTerminal

# 本企业用户验证信息


class VerifyUserInformation():

    # 添加新用户
    def set_user_information(request):
        data = json.loads(request.body)
        retdata = []
        local_uuid = data['local_uuid']
        return_uuid = data['ret_uuid']
        dev_uuid = data['dev_uuid']
        lenter_code = data['enter_code']
        u_name = make_password(
            data['user_name'], salt='980513', hasher='default')
        u_pwd = make_password(
            data['pass_word'], salt='1975217', hasher='default')
        show_name = data['show_name']
        user_permissions_code = UserPermissions.objects.filter(
            Q(permissions_name=data['user_permiss'])).values('permissions_code')

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
                res = User_local.objects.filter(
                    Q(username=u_name) & Q(enter_code=lenter_code)).count()
                if res == 0:
                    res = User_local.objects.create(username=make_password(
                        u_name, salt='980513', hasher='default'), password=make_password(
                        u_pwd, salt='1975217', hasher='default'), show_name=show_name, user_permissions=user_permissions_code, enter_code=lenter_code)
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
        retdata = []
        data = json.loads(request.body)
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
            retsql = User_local.objects.values(
                'id', 'user_phone', 'user_email', 'show_name', 'user_permissions').filter(Q(enter_code=lenter_code))
            res = {
                'status': 'OK',
                'info': '信息获取成功',
            }
            retdata = list(retsql.values())
            print(retdata)
            # retdata.insert(0, res)
            retdata_json = json.dumps(retdata)
            return HttpResponse(retdata_json)

    # 获取用户权限列表

    def get_user_permissions(request):
        retdata = []
        data = json.loads(request.body)
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
            retsql = UserPermissions.objects.all()
            res = {
                'status': 'OK',
                'info': '信息获取成功',
            }
            retdata = list(retsql.values())
            retdata.insert(0, res)
            retdata_json = json.dumps(retdata)
            return HttpResponse(retdata_json)

    # 用户登录验证

    def verify_user_information(request):
        retdata = []
        data = json.loads(request.body)
        local_uuid = data['local_uuid']
        return_uuid = data['ret_uuid']
        dev_uuid = data['dev_uuid']
        lenter_code = data['enter_code']
        u_name = make_password(
            data['user_name'], salt='980513', hasher='default')
        u_pwd = make_password(
            data['pass_wd'], salt='1975217', hasher='default')

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
                        Q(username=u_name) & Q(enter_code=lenter_code)).count()
                    if verify_user == 0:
                        res = {
                            'status': 'no',
                            'info': '此用户无法登录当前企业。',
                        }
                        retdata.append(res)
                        jsondata = json.dumps(retdata)
                        return HttpResponse(content=jsondata)
                    else:
                        verify_user = User_local.objects.filter(Q(username=u_name) & Q(
                            password=u_pwd) & Q(enter_code=lenter_code)).count()
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
                                password=u_pwd) & Q(enter_code=lenter_code))
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
                            try:
                                login_logs.objects.filter(Q(login_uuid=local_uuid) & Q(return_uuid=return_uuid) & Q(
                                    login_enter_code=lenter_code) & Q(login_dev_uuid=dev_uuid)).update(login_user_code=u_name)
                                return HttpResponse(content=jsondata)
                            except Exception as e:
                                res = {
                                    'status': 'no',
                                    'info': '更新验证数据失败！',
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
