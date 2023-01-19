from unittest.mock import MagicMock
from unittest import TestCase
from api.services.interfaces.task_services_interface import TaskServicesInterface
from api.services.exceptions import TaskApplicationException
from entities.task import Task
from application import create_app
import json


class TestTaskResource(TestCase):

    def conf(self, binder):
        self.task_app = MagicMock(TaskServicesInterface)
        binder.bind(TaskServicesInterface, to=self.task_app)

    def setUp(self) -> None:
        self.app = create_app(config=None, testing_modules_binding=[self.conf], configure_database=False, configure_scheduler=False)
        self.client = self.app.test_client()
        self.api_prefix = self.app.blueprints.get('cronos_api').url_prefix
        self.url = f'{self.api_prefix}/task'
        self.task_info = {
            'name': 'Testing',
            'description': 'Testing',
            'url': 'localhost:8000',
            'method': 'POST'
        }

    def test_post_when_no_data_then_return_400(self):
        response = self.client.post(self.url, data=json.dumps({}), content_type='application/json')
        self.assertEqual(400, response.status_code)
        response_data = response.get_json()
        self.assertEqual('MISSING_DATA', response_data['error_type'])
    
    def test_post_when_ok_then_return_200(self):
        task_response = Task(name='Testing', description='Testing', url='localhost:8000', method='POST')
        self.task_app.create_new_task.return_value = task_response

        response = self.client.post(
            f'{self.api_prefix}/task',
            data=json.dumps(self.task_info),
            content_type='application/json'
        )
        self.assertEqual(200, response.status_code)
