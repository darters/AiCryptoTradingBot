import pandas
import requests
from datetime import datetime

COIN = 'BTC'
INTERVAL = '1d'
# LIKE (YEAR-MONTH-DAY HOURS:MINUTES:SECONDS)
START_TIME = '2025-02-04 01:00:00'
END_TIME = '2025-02-05 01:00:00'

def fetch_candle_info():
    url = "https://api.hyperliquid.xyz/info"

    headers = {
        "Content-Type": "application/json"
    }
    start_time = int(datetime.strptime(START_TIME, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
    end_time = int(datetime.strptime(END_TIME, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
    print(start_time)
    print(end_time)
    data = {
        "req": {
            "coin": COIN, "interval": INTERVAL, "startTime": start_time, "endTime": end_time
        },
        "type": "candleSnapshot"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        data = response.json()
        return data
    except Exception as e:
        print(e)

def display_candle_info(data):
    if data == None:
        return

    displayed_data = pandas.DataFrame(data)
    displayed_data.rename(columns = {
        'T': 'Start-Time',
        't': 'End-Time',
        's': 'Coin',
        'i': 'Interval',
        'o': 'Open',
        'c': 'Close',
        'h': 'High',
        'l': 'Low',
        'v': 'Volume',
        'n': 'Number of Trades'
    }, inplace=True)
    displayed_data['Start-Time'] = pandas.to_datetime(displayed_data['Start-Time'], unit='ms')
    displayed_data['End-Time'] = pandas.to_datetime(displayed_data['End-Time'], unit='ms')

    return displayed_data


def main():
    candle_info = fetch_candle_info()
    print(display_candle_info(candle_info))


if __name__ == "__main__":
    main()

