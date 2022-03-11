from notice import models


#  前端页面全局需要的对象
# notice menu
def unreads(request):
    if request.session.get('phone'):
        unreads = models.Notice.objects.filter(is_read=False)
    else:
        unreads = ''
    return {'unreads': unreads}


def messages(request):
    if request.session.get('phone'):
        messages = models.Message.objects.all()
    else:
        messages = ''
    return {'messages': messages}