from conf import models


#  前端页面全局需要的对象
# conf menu
def conf_types(request):
    if request.session.get('phone'):
        conf_types = models.Type.objects.all()
    else:
        conf_types = ''
    return {'conf_types': conf_types}