from django.test import TestCase
from script import models
from member import models as member_models

# Create your tests here.


class ScriptModelsTestCase(TestCase):

    def setUp(self):
        print("创建模型")
        user = member_models.User.objects.create(
            name='test', gender='male', phone='1000000001', email='test@email.com', password='123456')
        language = models.Language.objects.create(name='ruby')

        models.Script.objects.create(
            alias='ruby', name='ruby', content='ruby.rb', language=language, author=user)

    def test_get_models(self):
        print("查询模型测试")
        models.Script.objects.filter(name='ruby')

    def test_update_modes(self):
        print("更新模型测试")
        models.Script.objects.filter(
            name='ruby').update(name='ruby2')
        print(models.Script.objects.get(name='ruby2').name)

    def test_del_models(self):
        print("删除模型测试")
        models.Script.objects.filter(name='ruby').delete()

    def tearDown(self):
        print("测试结束")
