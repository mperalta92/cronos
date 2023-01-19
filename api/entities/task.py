from enum import Enum
from flask_restx import fields
from datetime import datetime
from entities.periodicity import Periodicity
import pytz


class TaskMethods(Enum):
    GET = 0
    POST = 1



task_fields = {
    'id': fields.Integer,
    'created_at': fields.DateTime(attribute=lambda x: x.created_at if x.created_at.tzinfo else pytz.utc.localize(x.created_at)),
    'name': fields.String(attribute=lambda x: x.name),
    'description': fields.String(attribute=lambda x: x.description),
    'url': fields.String,
    'method': fields.String(attribute=lambda x: x.method)
}

class Task:
    """
    This class handle a task object and 
    """

    def __init__(self,
                name: str,
                description: str,
                url: str,
                method: TaskMethods = TaskMethods.GET,
                params: str = "",
                body: str = ""
                ):
        self.created_at = datetime.now()
        self.name = name
        self.description = description
        self.url = url
        self.method = method
        self.params = params
        self.body = body
        self.is_deleted = False
        self.deleted_at = None
        self.periodicity = None

    def set_periodicity(self, periodicity: Periodicity):
        self.periodicity = periodicity









