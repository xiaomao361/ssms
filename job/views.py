import imp
from pyexpat import model
from django.shortcuts import render
from job import models
from member import models as member_models
from property import models as property_models
from script import models as script_models
from conf import models as conf_models
import subprocess
from django.shortcuts import HttpResponse
import json
import re
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job


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


# 执行脚本接口
def exec_script(request):
    # get id from front
    if request.GET.get('exec_user_name') and request.GET.getlist('servers_id') and request.GET.get('script_id') and request.GET.get('playbook_id'):
        exec_user_name = request.GET.get('exec_user_name')
        servers_id = request.GET.getlist('servers_id')
        script_id = request.GET.get('script_id')
        playbook_id = request.GET.get('playbook_id')

        result = run_script(exec_user_name, servers_id, script_id, playbook_id)
        return HttpResponse(json.dumps(result))


# 执行脚本的方法
def run_script(user, servers_id, script_id, playbook_id):

    # 命令及文件
    ansible = '/usr/local/bin/ansible-playbook'
    hosts_file = './tmp/tmp_hosts'
    script_file = './tmp/tmp_script'
    playbook_file = './tmp/tmp_platbook.yml'

    # make hosts file
    hosts = []
    for server_id in servers_id:
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

    cmd = ansible-playbook + ' -i ' + hosts + \
        ' ' + playbook + ' -e ' + ' user=' + user

    result = subprocess.getoutput(cmd)

    return result


# 定时任务
# 开启定时工作
try:
    # 实例化调度器
    scheduler = BackgroundScheduler()
    # 调度器使用DjangoJobStore()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # 设置定时任务，选择方式为interval，时间间隔为10s
    # @register_job(scheduler,"interval", seconds=10)
    # 另一种方式为每天固定时间执行任务，对应代码为：
    # @register_job(scheduler, 'cron', day_of_week='mon-fri', hour='9', minute='30', second='10',id='task_time', replace_existing=True)
    tasks = models.CronTask.objects.all()
    for task in tasks:
        print(task.type, task.day_of_week, task.hour,
              task.minute, task.second, task.name)
        
        if task.type == 'cron':
            @register_job(scheduler, task.type, day_of_week=task.day_of_week, hour=task.hour, minute=task.minute, second=task.second, id=task.name, replace_existing=True)
            def my_job():
                print(task.user, task.servers, task.script, task.playbook)
                # run_script(user=task.user, servers_id=task.servers,
                #           script_id=task.script, playbook_id=task.playbook)
        elif task.type == 'interval':
            @register_job(scheduler,"interval", seconds=int(task.second), id=task.name, replace_existing=True)
            def my_job():
                print(task.user, task.servers, task.script, task.playbook)
                # run_script(user=task.user, servers_id=task.servers,
                #           script_id=task.script, playbook_id=task.playbook)
    register_events(scheduler)
    scheduler.start()
except Exception as e:
    print(e)
    # 有错误就停止定时器
    scheduler.shutdown()
