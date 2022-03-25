import imp
from django.test import TestCase
from member import models

class MemberModelsTestCase(TestCase):
    
    def setUp(self):
        print("创建模型")
        models.User.objects.create(
            name='test', gender='male', phone='1000000001', email='test@email.com', password='123456')
        models.ExecUser.objects.create(
            name='test', username='test')

    def test_get_models(self):
        print("查询模型测试")
        print(models.User.objects.get(name='test').phone)
        print(models.ExecUser.objects.get(name='test').username)

    def test_update_modes(self):
        print("更新模型测试")
        models.User.objects.filter(name='test').update(name='test1')
        print(models.User.objects.get(name='test1').name)
    
    def test_del_models(self):
        print("删除模型测试")
        models.User.objects.filter(name='test').delete()

    def tearDown(self):
        print("测试结束")
