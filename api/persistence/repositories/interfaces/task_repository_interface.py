from abc import ABC, abstractmethod


class TaskRepositoryInterface(ABC):

    @abstractmethod
    def save_task(self, task):
        pass
