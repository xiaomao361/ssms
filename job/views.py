from django.shortcuts import render
from member import models as member_models
from property import models as property_models
import subprocess
from django.shortcuts import HttpResponse
import json
import re


# Create your views here.
# 命令列表
def cmd(request):
    exec_users = member_models.ExecUser.objects.all()
    servers = property_models.Server.objects.all()
    return render(request, 'job/cmd.html',
                  {'exec_users': exec_users,
                   'servers': servers})


# 批量命令执行方法
def exec_cmd(request):

    # ansible 命令及hosts文件配置
    ansible = '/usr/local/bin/ansible'
    hosts = './tmp/hosts'

    if request.GET.get('exec_user_name') and request.GET.getlist('servers') and request.GET.get('command'):
        exec_user_name = request.GET.get('exec_user_name')
        servers = request.GET.getlist('servers')
        command = request.GET.get('command')
        exec_servers = ''
        for server in servers:
            exec_servers = str(server) + ' ' + exec_servers

        cmd = ansible + ' -i ' + hosts + ' ' + \
            '"' + exec_servers + '"' + ' ' + '-m shell' + ' ' + '-a' + ' ' + \
            '"' + command + '"' + ' -u ' + exec_user_name

        result = subprocess.getoutput(cmd)
        return HttpResponse(json.dumps(result))
