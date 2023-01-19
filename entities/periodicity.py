from calendar import month
from datetime import time, datetime, timedelta
from dateutil.relativedelta import relativedelta
from functools import reduce
from typing import List
from flask_restx import fields


periodicity_fields = {
    'days_in_month': fields.List(fields.Integer),
    'days_in_week': fields.List(fields.Integer),
    'list_of_times': fields.List(fields.String(attribute=lambda x: f"{x.hour}:{x.minute}")),
}

class Periodicity:
    """
    This class handle the tasks periodicity
    params:
    days_in_month List[int] --> List of days in a month according to their number [(-20)-31]
    days_in_week List[int] --> list of days in a week according to their number [1-7]
    
    """

    def __init__(self,
                days_in_month: List[int],
                days_in_week: List[int],
                list_of_times: List[time]
                ):
        self.days_in_month = days_in_month
        self.days_in_week = days_in_week
        self.list_of_times = list_of_times

    def is_a_valid_datetime(self, datetime_instance: datetime) -> bool:
        depure_days_in_month = self.depure_negative_days_of_month(datetime_instance=datetime_instance)
        valid_day_in_month = True if datetime_instance.day in depure_days_in_month else False
        valid_day_in_week = True if datetime_instance.weekday()+1 in self.days_in_week else False
        time_compare = lambda x: x.hour == datetime_instance.hour and x.minute == datetime_instance.minute
        valid_time = reduce(lambda x, y: x or y, list(map(time_compare, self.list_of_times)))
        return (valid_day_in_month or valid_day_in_week) and valid_time

    def depure_negative_days_of_month(self, datetime_instance: datetime):
        depure_days_in_month = []
        for day in self.days_in_month:
            depure_day = day
            if day <= 0:
                corrected_datetime = datetime_instance - timedelta(days=(datetime_instance.day-1)) + relativedelta(months=1)
                corrected_datetime -= timedelta(days=abs(day))
                depure_day = corrected_datetime.day
            depure_days_in_month.append(depure_day)
        return depure_days_in_month

