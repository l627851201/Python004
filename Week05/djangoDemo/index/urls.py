"""djangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, register_converter
from . import views,converters

register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index),

    # 带变量的URL
    # path('<int:year>', views.year),
    path('<int:year>/<str:name>', views.name),

    # 正则表达式
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

    # 自定义过滤器
    path('<yyyy:year>', views.year_diy),

]

