from ast import alias
from cv2 import CAP_GIGANETIX
from django.test import TestCase
from django.test import Client
from conf.models import Type, Conf
from member import models as member_models


class ConfModelsTestCase(TestCase):

    def setUp(self):
        print("创建模型")
        # 新增模型
        user = member_models.User.objects.create(
            name='test', gender='male', phone='1000000001', email='test@email.com', password='123456')
        type = Type.objects.create(name="test", extension="xyz")
        Conf.objects.create(alias="other", name="无尽的测试",
                            content="啊玛尼玛尼呗呗轰", type=type, author=user)

    def test_get_models(self):
        print("查询模型测试")
        print(Type.objects.get(name='test').extension)
        print(Conf.objects.get(alias='other').content)

    def test_update_modes(self):
        print("更新模型测试")
        Type.objects.filter(name='test').update(name='test1')
        print(Type.objects.get(name='test1').name)
    
    def test_del_models(self):
        print("删除模型测试")
        Type.objects.filter(name='test').delete()

    def tearDown(self):
        print("测试结束")
