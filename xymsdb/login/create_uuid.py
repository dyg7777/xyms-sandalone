# -*- coding: UTF-8 -*-
"""=================================================
@文件名  : 粮食收储管理系统 -> make_encrypt_code
@编程语言:  Python
@作者    : 耿春雨先生
@日期    :  2023/08/31 15:35
@权利信息 ：本信息以下所有代码均归属哈尔滨市双城区鑫奕科创电脑服务中心所有版权归属于耿春雨先生。
=================================================="""
import uuid


class Encrypt_code():
    def make_encrypt_code(self, incode):  # 根据客户端传来的验证码生成唯一码，用于后续客户端操作验证时候为本机用
        out_id = uuid.uuid5(uuid.NAMESPACE_URL, str(incode) + '1975217')
        return str(out_id)
