"""
URL configuration for xymsdb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import InitialValidation
from .verify_user import VerifyUserInformation

urlpatterns = [
    path(r'get_enterprise_information/',
         InitialValidation.get_enterprise_information),  # 获取企业信息
    path(r'get_user_informations/',
         InitialValidation.get_user_information),  # 获取用户库是否为空
    path(r'set_user_information/',
         VerifyUserInformation.set_user_information),  # 创建用户
    path(r'verify_user_information/',
         VerifyUserInformation.verify_user_information),  # 用户登录验证
]
