from member import models


#  前端页面全局需要的对象
def user(request):
    if request.session.get('phone'):
        phone = request.session.get('phone')
        user = models.User.objects.get(phone=phone)
    else:
       user = ''
    return {'user': user}
