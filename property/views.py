import imp
from django.shortcuts import render, redirect
from property import models
from member import models as member_models
import os
import subprocess


# Create your views here.
# 服务器列表
def servers(request):
    servers = models.Server.objects.all().order_by("c_time")
    return render(request, 'property/servers.html',
                  {'servers': servers, })


def ping(request):

    # ansible 命令及hosts文件配置
    ansible = '/usr/local/bin/ansible'
    hosts = './media/system/hosts'

    if request.GET.get('server_id'):
        server_id = request.GET.get('server_id')
        server = models.Server.objects.get(id=server_id)
        user = member_models.ExecUser.objects.get(name=server.exec_user).name
        cmd = ansible + ' -i ' + hosts + ' ' + \
            server.name + ' ' + '-m ping' + ' -u ' + user
        try:
            result = subprocess.check_output(cmd, shell=True)
            if len(result) > 0:
                if server.is_online == False:
                    models.Server.objects.filter(id=server_id).update(is_online=True)
            elif server.is_online == True:
                models.Server.objects.filter(id=server_id).update(is_online=False)
        except Exception as e:
            result = e
    servers = models.Server.objects.all()  # 这部分写的太二了，考虑重置，先实现功能
    return render(request, 'property/servers.html',
                  {'servers': servers,
                   'result': result, })
