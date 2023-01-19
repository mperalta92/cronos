from enum import Enum
from xmlrpc.client import SYSTEM_ERROR

class TaskApplicationException(Exception):
    class ErrorType(Enum):
        SYSTEM_ERROR = 0
        DATABASE_ERROR = 1
        TASK_NOT_FOUND = 2

    def __init__(self, error_type: ErrorType = ErrorType.SYSTEM_ERROR, message=None):
        self.error_type = error_type
        self.message = message
        super().__init__(self.message)