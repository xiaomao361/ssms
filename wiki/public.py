from wiki import models


#  前端页面全局需要的对象
# wiki menu
def categorys(request):
    if request.session.get('phone'):
        categorys = models.Category.objects.all()
    else:
        categorys = ''
    return {'categorys': categorys}