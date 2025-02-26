import re
import sys
from utils.validator import Validator
from datetime import datetime

def get_user_input():
    data = input("Enter: symbol, interval, start_time, end_time, quantity (e.g., BTCUSDT, 1h, 2025-02-18 08:00:00, current_time, 0.2): ").strip()

    exp = r"(\d{4}-\d{2}-\d{2})(\d{2}:\d{2}:\d{2})"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fields = re.sub(r'\s+', '', data).split(',')
    if len(fields) != 5:
        sys.exit(ValueError("📢 You must enter 5 values"))
 
    symbol = fields[0].upper()
    interval = fields[1]
    start_time = fields[2]
    end_time = fields[3]
    if(end_time == 'current_time'):
        end_time = current_time
    quantity = float(fields[4])
    start_time = re.sub(exp, r"\1 \2", start_time)
    end_time = re.sub(exp, r"\1 \2", end_time)

    Validator.check_values(interval, start_time, end_time, current_time, quantity)
    return symbol, interval, start_time, end_time, quantity
    
