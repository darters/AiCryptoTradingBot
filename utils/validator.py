import re
from datetime import datetime

class Validator:
    INTERVALS = frozenset(['1m', '3m', '5m', '15m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M'])
    PATTERN = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"

    @staticmethod
    def check_values(interval, start_time, end_time, current_time, quantity):
        try: 
            Validator.quantity_check(quantity)
        except ValueError as e:
            print(e)
            exit(1)            
        try: 
            Validator.interval_check(interval)
        except ValueError as e:
            print(e)
            exit(1)            
        try: 
            Validator.datetime_check(start_time, end_time, current_time)
        except ValueError as e:
            print(e)
            exit(1)            

    @staticmethod
    def quantity_check(quantity):
        if quantity < 0.01:
            raise ValueError(f"📢 Invalid quantity, quantity must be more than 0.01")
    @staticmethod
    def interval_check(interval):
        if interval not in Validator.INTERVALS:
            raise ValueError(f"📢 Invalid interval, interval must be one of {Validator.INTERVALS}")
        return True
    @staticmethod
    def datetime_check(start_time, end_time, current_time):
        start_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end_dt = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        current_dt = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")

        if current_dt < end_dt:
            raise ValueError(f"📢 Invalid end_time, end_time must be less than current time")
        if end_dt < start_dt:
            raise ValueError(f"📢 Invalid end time, end time must be more than start time")        
        if not re.match(Validator.PATTERN, start_time) or not re.match(Validator.PATTERN, end_time):
            raise ValueError(f"📢 Invalid datetime")
        return True
