from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        first_date = datetime.strptime(date1, '%Y-%m-%d').date()
        second_date = datetime.strptime(date2, '%Y-%m-%d').date()

        return abs((first_date - second_date).days)
