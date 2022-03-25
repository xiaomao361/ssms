from statistics import mode
from django.shortcuts import render
from conf import models
from django.shortcuts import HttpResponse
import json
import subprocess


# 配置列表页
def list(request):
    if request.GET.get('type_id'):
        type_id = request.GET.get('type_id')
        type = models.Type.objects.get(id=type_id)
        confs = models.Conf.objects.filter(type=type)
    else:
        type = ''
        confs = ''
    return render(request, 'conf/list.html',
                  {'type': type,
                   'confs': confs})


# 配置内容页
def content(request):
    if request.GET.get('conf_id'):
        conf_id = request.GET.get('conf_id')
        content = models.Conf.objects.get(id=conf_id)
    else:
        content = ''
    return render(request, 'conf/content.html',
                  {'content': content})


# 生成文件
def make_file(request):
    data = {}
    if request.GET.get('conf_id'):
        conf_id = request.GET.get('conf_id')
        conf = models.Conf.objects.get(id=conf_id)
        type = models.Type.objects.get(name=conf.type)
        # 确定文件后缀名
        if str(conf.type) == 'hosts':
            file_name = './tmp/'  + conf.name  
        else:
            file_name = './tmp/files/'  + conf.name  + '.' + type.extension
        
        try:
            with open(file_name, "w+", newline='') as f:
                f.write(conf.content)
            f.close()

            # 移除第一行及最后一行，markdown格式代码块标记
            # for mac
            cmd = "sed -i '' '1d' " + file_name + ' && ' + "sed -i '' '$d' " + file_name
            # fir linux 
            # cmd = "sed -i  '1d' " + file_name + ' && ' + "sed -i  '$d' " + file_name

            subprocess.getoutput(cmd)
            data.update(status='success')
        except Exception as e:
            data.update(status=e)
    else:
        data.update(status='error')
    
    return HttpResponse(json.dumps(data))
