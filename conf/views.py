from django.shortcuts import render
from conf import models

# Create your views here.
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