from ast import alias
import imp
from multiprocessing import AuthenticationError
from pkgutil import ImpImporter
from django.test import TestCase
from job import models
from conf import models as conf_models
from job.views import script
from member import models as member_models
from script import models as script_models
from property import models as property_models
from conf import models as conf_models

# Create your tests here.


class JobModelsTestCase(TestCase):

    def setUp(self):
        print("创建模型")
        # 新增模型
        user = member_models.User.objects.create(
            name='test', gender='male', phone='1000000001', email='test@email.com', password='123456')
        exec_user = member_models.ExecUser.objects.create(
            name='test', username='test')
        server = property_models.Server.objects.create(
            name='test', ip='192.168.1.100', ssh_port='22', exec_user=exec_user, os='centos')
        language = script_models.Language.objects.create(name='ruby')
        
        script = script_models.Script.objects.create(
            alias='ruby', name='ruby', content='ruby.rb', language=language, author=user)
        type = conf_models.Type.objects.create(name="xyz", extension="xyz")
        playbook = conf_models.Conf.objects.create(alias="other", name="playbook",
                            content="wtf", type=type, author=user)
        task = models.CronTask.objects.create(name='无尽的测试定时任务', type='interval',
                                       second='10', user=exec_user, script=script, playbook=playbook)
        task.servers.add(server)

    def test_get_models(self):
        print("查询模型测试")
        models.CronTask.objects.filter(name='无尽的测试定时任务')

    def test_update_modes(self):
        print("更新模型测试")
        models.CronTask.objects.filter(name='无尽的测试定时任务').update(name='无尽的测试定时任务2')
        print(models.CronTask.objects.get(name='无尽的测试定时任务2').name)

    def test_del_models(self):
        print("删除模型测试")
        models.CronTask.objects.filter(name='无尽的测试定时任务').delete()

    def tearDown(self):
        print("测试结束")
