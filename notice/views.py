from django.shortcuts import render
from notice import models


# Create your views here.
# 系统通知列表页
def list(request):
    notices = models.Notice.objects.all()
    if not notices:
        notices = ''
    return render(request, 'notice/list.html',
                  {'notices': notices})


# 系统通知内容页
def content(request):
    if request.GET.get('notice_id'):
        notice_id = request.GET.get('notice_id')
        content = models.Notice.objects.get(id=notice_id)
        if not content.is_read:
            models.Notice.objects.filter(id=notice_id).update(is_read=True)
    else:
        content = ''
    return render(request, 'notice/content.html',
                  {'content': content})
