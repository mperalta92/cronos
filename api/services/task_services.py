from api.services.interfaces.task_services_interface import TaskServicesInterface
from persistence.repositories.interfaces.task_repository_interface import TaskRepositoryInterface
from api.services.exceptions import TaskApplicationException
from entities.task import Task
from typing import Dict
from injector import inject

class TaskApplication(TaskServicesInterface):

    @inject
    def __init__(self, task_repository: TaskRepositoryInterface) -> None:
        self.task_repository: task_repository

    def create_new_task(self, task_info: Dict) -> Task:
        task_instance = Task(
            name=task_info.get('name'),
            description=task_info.get('description'),
            url=task_info.get('url'),
            method=task_info.get('method')
        )
        try:
            self.task_repository.save_task(task=task_instance)
        except Exception as e:
            raise TaskApplicationException(error_type=TaskApplicationException.ErrorType.DATABASE_ERROR)
        return task_instance