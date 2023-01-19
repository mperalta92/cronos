from abc import ABC, abstractmethod
from typing import List, Dict
from entities.task import Task

class TaskServicesInterface(ABC):

    @abstractmethod
    def create_new_task(self, task_info: Dict) -> Task:
        pass