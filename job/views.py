import imp
from django.shortcuts import render
from member import models as member_models
from property import models as property_models
from script import models as script_models
from conf import models as conf_models
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


# 命令列表
def script(request):
    exec_users = member_models.ExecUser.objects.all()
    servers = property_models.Server.objects.all()
    scripts = script_models.Script.objects.all()
    confs = conf_models.Conf.objects.all()
    return render(request, 'job/script.html',
                  {'exec_users': exec_users,
                   'servers': servers,
                   'scripts': scripts,
                   'confs': confs})


# 执行脚本方法
def exec_script(request):

    # 命令及文件
    ansible = '/usr/local/bin/ansible-playbook'
    hosts_file = './tmp/tmp_hosts'
    script_file = './tmp/tmp_script'
    playbook_file = './tmp/tmp_platbook.yml'

    # get id from front
    if request.GET.get('exec_user_name') and request.GET.getlist('server_ids') and request.GET.get('script_id') and request.GET.get('playbook_id'):
        exec_user_name = request.GET.get('exec_user_name')
        server_ids = request.GET.getlist('server_ids')
        script_id = request.GET.get('script_id')
        playbook_id = request.GET.get('playbook_id')

         # make hosts file
        hosts = []
        for server_id in server_ids:
            server = property_models.Server.objects.get(id=server_id)
            hosts.append("[server.name]")
            hosts.append(server.id)

        try:
            with open(hosts_file, "w+", newline='') as f:
                for line in hosts:
                    f.write(line)
            f.close()
        except Exception as e:
            print(e)

        # make script file
        script = script_models.Script.objects.get(id=script_id)
        try:
            with open(script_file, "w+", newline='') as f:
                f.write(script.content)
            f.close()
        except Exception as e:
            print(e)

        # make playbook file
        playbook = conf_models.Conf.objects.get(id=playbook_id)
        try:
            with open(playbook_file, "w+", newline='') as f:
                f.write(script.content)
            f.close()
        except Exception as e:
            print(e)

        cmd = ansible-playbook + ' -i ' + hosts + ' ' + playbook 

        result = subprocess.getoutput(cmd)
        return HttpResponse(json.dumps(result))
