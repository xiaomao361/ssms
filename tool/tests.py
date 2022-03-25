import imp
from unicodedata import name
from django.test import TestCase
from tool import models

class ToolModelsTestCase(TestCase):
    
    def setUp(self):
        print("创建模型")
        models.Site.objects.create(
            name='test', url='https://www.test.com', description='一个测试网站')

    def test_get_models(self):
        print("查询模型测试")
        print(models.Site.objects.get(name='test').url)
       

    def test_update_modes(self):
        print("更新模型测试")
        models.Site.objects.filter(name='test').update(name='test1')
        print(models.Site.objects.get(name='test1').name)
    
    def test_del_models(self):
        print("删除模型测试")
        models.Site.objects.filter(name='test').delete()

    def tearDown(self):
        print("测试结束")
