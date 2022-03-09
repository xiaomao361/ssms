from django.shortcuts import render
from wiki import models
import wiki


# Create your views here.
# 维基类型页面
def list(request):
    if request.GET.get('category_id'):
        category_id = request.GET.get('category_id')
        category = models.Category.objects.get(id=category_id)
        wikis = models.Wiki.objects.filter(category=category_id)
    else:
        wikis = ''
        category = ''
    return render(request, 'wiki/list.html',
                  {'wikis': wikis,
                  'category': category})


# 维基内容页面
def content(request):
    if request.GET.get('wiki_id'):
        wiki_id = request.GET.get('wiki_id')
        number = models.Wiki.objects.get(id=wiki_id).number
        number += 1  # 增加阅读次数
        models.Wiki.objects.filter(id=wiki_id).update(number=number)
        content = models.Wiki.objects.get(id=wiki_id)
    else:
        content = ''
    return render(request, 'wiki/content.html',
                  {'content': content})
