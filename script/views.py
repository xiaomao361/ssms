from django.shortcuts import render
from script import models


# Create your views here.
# 脚本列表页
def list(request):
    if request.GET.get('language_id'):
        language_id = request.GET.get('language_id')
        language = models.Language.objects.get(id=language_id)
        scripts = models.Script.objects.filter(language=language)
    else:
        language = ''
        scripts = ''
    return render(request, 'script/list.html',
                  {'language': language,
                  'scripts': scripts})


# 脚本内容页
def content(request):
    if request.GET.get('script_id'):
        script_id = request.GET.get('script_id')
        content = models.Script.objects.get(id=script_id)
    else:
        content = ''
    return render(request, 'script/content.html',
                  {'content': content})