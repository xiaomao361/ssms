import imp
import re
from django.shortcuts import render
from property import models
from member import models as member_models
import os
import subprocess
from django.shortcuts import HttpResponse
import json


# Create your views here.
# 服务器列表
def servers(request):
    servers = models.Server.objects.all().order_by("c_time")
    return render(request, 'property/servers.html',
                  {'servers': servers, })


def ping(request):

    # ansible 命令及hosts文件配置
    ansible = '/usr/local/bin/ansible'
    hosts = './tmp/hosts'

    if request.GET.get('server_id'):
        server_id = request.GET.get('server_id')
        server = models.Server.objects.get(id=server_id)
        user = member_models.ExecUser.objects.get(name=server.exec_user).name
        cmd = ansible + ' -i ' + hosts + ' ' + \
            server.name + ' ' + '-m ping' + ' -u ' + user

    result = subprocess.getoutput(cmd)
    status = re.findall(r'.\|(.*)\=>.',result)
    if re.sub(' ','', status)  == 'SUCCESS':
        if server.is_online == False:
            models.Server.objects.filter(id=server_id).update(is_online=True)
    else:
        if server.is_online == True:
            models.Server.objects.filter(id=server_id).update(is_online=False)

    data = {}
    data.update(ip=server.ip)
    data.update(result=result[result.index("{"):])
    return HttpResponse(json.dumps(data))
