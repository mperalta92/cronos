from datetime import datetime, timedelta


class TaskLog:
    """
    This class contains task execution responses.
    """

    def __init__(self,
                task_id: int,
                task_name: str,
                started_at: datetime,
                duration: timedelta,
                task_response_code: int,
                task_response_body: str
                ):
        self.created_at = datetime.now()
        self.task_id = task_id        
        self.task_name = task_name
        self.started_at = started_at
        self.duration = duration
        self.task_response_code = task_response_code
        self.task_response_body = task_response_body
