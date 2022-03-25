from pyexpat import model
from statistics import mode
from django.test import TestCase
from wiki import models
from member import models as member_models



class WikiModelsTestCase(TestCase):

    def setUp(self):
        print("创建模型")
        user = member_models.User.objects.create(
            name='test', gender='male', phone='1000000001', email='test@email.com', password='123456')
        type = models.Category.objects.create(type='test')
        models.Wiki.objects.create(title='test', content='一个测试的维基', category=type, author=user)

    def test_get_models(self):
        print("查询模型测试")
        print(models.Wiki.objects.get(title='test').content)

    def test_update_modes(self):
        print("更新模型测试")
        models.Wiki.objects.filter(title='test').update(title='test1')
        print(models.Wiki.objects.get(title='test1').title)

    def test_del_models(self):
        print("删除模型测试")
        models.Wiki.objects.filter(title='test').delete()

    def tearDown(self):
        print("测试结束")
