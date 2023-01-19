from flask import request
from flask_restx import Resource, marshal
from injector import inject
from api.services.exceptions import TaskApplicationException
from api.services.interfaces.task_services_interface import TaskServicesInterface
from entities.task import task_fields
from api.resources.serializers import task_data
from api.restx import api


class TaskResource(Resource):

    @inject
    def __init__(self, application: TaskServicesInterface, **kwargs):
        self.application = application
        self.api = api

    @api.expect(task_data)
    def post(self):
        """
        This method create a new task and return the task data
        """
        data = request.get_json()
        try:
            if not data:
                return {'error_type': 'MISSING_DATA'}, 400

            result = self.application.create_new_task(task_info={
                'name': data.get('name'),
                'description': data.get('description'),
                'url': data.get('url'),
                'method': data.get('method')
            })
            
        except TaskApplicationException as e:
            return {'error_type': e.error_type.name, 'message': e.message}, 501
        except Exception as e:
            return {'error_type': 'UNHANDLED_ERROR'}, 500
        try:
            return {'data': marshal(result, task_fields)}, 200
        except Exception:
            return {'error_type': 'MARSHAL_ERROR'}, 500