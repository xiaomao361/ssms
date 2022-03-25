from ast import alias
from cv2 import CAP_GIGANETIX
from django.test import TestCase
from django.test import Client
from conf.models import Type, Conf
from member import models as member_models


class TypeTestCase(TestCase):

    def setUp(self):
        print("创建模型")
        user = member_models.User.objects.create(
            name='test', gender='male', phone='1000000001', email='test@email.com', password='123456')
        type = Type.objects.create(name="test", extension="xyz")
        Conf.objects.create(alias="other", name="无尽的测试",
                            content="啊玛尼玛尼呗呗轰", type=type, author=user)

    def test_get_models(self):
        print(Type.objects.get(name='test').extension)
        print(Conf.objects.get(alias='other').content)

    def tearDown(self):
        print("模块测试结束")
