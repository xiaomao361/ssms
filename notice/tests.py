from django.test import TestCase
from notice import models

class NoticeModelsTestCase(TestCase):
    
    def setUp(self):
        print("创建模型")
        models.Notice.objects.create(
            title='test', content='通知测试')

    def test_get_models(self):
        print("查询模型测试")
        print(models.Notice.objects.get(title='test').content)
       

    def test_update_modes(self):
        print("更新模型测试")
        models.Notice.objects.filter(title='test').update(title='test1')
        print(models.Notice.objects.get(title='test1').title)
    
    def test_del_models(self):
        print("删除模型测试")
        models.Notice.objects.filter(title='test').delete()

    def tearDown(self):
        print("测试结束")