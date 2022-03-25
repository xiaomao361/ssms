from django.test import TestCase
from property import models
from member import models as member_models


class PropertyModelsTestCase(TestCase):

    def setUp(self):
        print("创建模型")
        # 新增模型
        exec_user = member_models.ExecUser.objects.create(
            name='test', username='test')
        models.Server.objects.create(
            name='test', ip='192.168.1.100', ssh_port='22', exec_user=exec_user, os='centos')

    def test_get_models(self):
        print("查询模型测试")
        print(models.Server.objects.get(name='test').ip)
       

    def test_update_modes(self):
        print("更新模型测试")
        models.Server.objects.filter(name='test').update(name='test1')
        print(models.Server.objects.get(name='test1').name)

    def test_del_models(self):
        print("删除模型测试")
        models.Server.objects.filter(name='test').delete()

    def tearDown(self):
        print("测试结束")
