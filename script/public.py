from script import models


#  前端页面全局需要的对象
# script menu
def languages(request):
    if request.session.get('phone'):
        languages = models.Language.objects.all()
    else:
        languages = ''
    return {'languages': languages}