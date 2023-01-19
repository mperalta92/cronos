from flask_restx import fields
from api.restx import api

task_data = api.model('task_data', {
    'name': fields.String(required=True, description='Task name'),
    'description': fields.String(required=True, description='Task description'),
    'url': fields.String(required=True, description='Task endpoint url'),
    'method': fields.String(required=True, description='Task endpoint method'),
})