import imp
import re
from django.shortcuts import render
from property import models
from member import models as member_models
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
    # result 输入成功及失败样式

    # success:

    #     192.168.0.240 | SUCCESS => {
    #     "ansible_facts": {
    #         "discovered_interpreter_python": "/usr/bin/python"
    #     },
    #     "changed": false,
    #     "ping": "pong"
    #       }

    # failed

    # 192.168.0.250 | UNREACHABLE! => {
    # "changed": false,
    # "msg": "Failed to connect to the host via ssh: ssh: connect to host 192.168.0.250 port 22: Connection refused",
    # "unreachable": true
    # }

    # 取 "|" 与 "=>" 中间的值
    status = re.findall(r'.\|(.*)\=>.', result)  # 获取状态 SUCCESS 或者 UNREACHABLE！

    # status是一个list对象，取第一个值转为字符串后，移除空格做判断

    if str(status[0]).strip() == 'SUCCESS':
        if server.is_online == False:
            # 如果命令执行成功，并且服务器在线状态不在线的时候，更新状态为在线
            models.Server.objects.filter(id=server_id).update(is_online=True)
    elif server.is_online == True:
        # 如果命令执行失败，并且服务器在线状态为在线的时候，更新状态为离线
        models.Server.objects.filter(id=server_id).update(is_online=False)

    #  构建给ajax返回的json字典
    data = {}
    data.update(ip=server.ip)
    data.update(result=result[result.index("{"):])

    return HttpResponse(json.dumps(data))
