from datetime import datetime, time
from unittest import TestCase
from unittest.mock import MagicMock
from typing import List
from api.entities.periodicity import Periodicity


class TestPeriodicity(TestCase):

    def setUp(self) -> None:
        self.periodicity = Periodicity(
            days_in_month=[1, 5, -1],
            days_in_week=[2, 6],
            list_of_times=[
                time(hour=1, minute=0),
                time(hour=2, minute=10),
                time(hour=3, minute=20)
                ]
        )

    def test_is_a_valid_datetime(self):
        test_datetimes_trues = [
            datetime(year=2022, month=1, day=1, hour=1, minute=0),
            datetime(year=2022, month=1, day=5, hour=1, minute=0),
            datetime(year=2022, month=10, day=8, hour=1, minute=0),
            datetime(year=2022, month=9, day=30, hour=1, minute=0),
            datetime(year=2022, month=1, day=1, hour=2, minute=10),
            datetime(year=2022, month=10, day=8, hour=2, minute=10),
            datetime(year=2022, month=1, day=1, hour=3, minute=20),
            datetime(year=2022, month=10, day=8, hour=3, minute=20),
        ]
        for test_datetime in test_datetimes_trues:
            self.assertTrue(
                self.periodicity.is_a_valid_datetime(datetime_instance=test_datetime)
                )
        test_datetimes_falses = [
            datetime(year=2022, month=1, day=1, hour=1, minute=10),
            datetime(year=2022, month=10, day=8, hour=1, minute=10),
            datetime(year=2022, month=1, day=2, hour=1, minute=0),
            datetime(year=2022, month=1, day=30, hour=1, minute=0),
        ]
        for test_datetime in test_datetimes_falses:
            self.assertFalse(
                self.periodicity.is_a_valid_datetime(datetime_instance=test_datetime)
                )

    def test_depure_negative_days_of_month(self):
        test_datetimes = [
            (datetime(year=2022, month=1, day=31, hour=1, minute=0), 31),
            (datetime(year=2022, month=2, day=5, hour=1, minute=0), 28),
            (datetime(year=2022, month=4, day=8, hour=1, minute=0), 30),
        ]
        for test_datetime, last_date in test_datetimes:
            days_result = self.periodicity.depure_negative_days_of_month(datetime_instance=test_datetime)
            self.assertListEqual(days_result, [1, 5, last_date])
            


    