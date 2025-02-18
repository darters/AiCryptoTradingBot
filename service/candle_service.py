import pandas
import requests
from datetime import datetime

COLUMNS = ["Open time", "Open price", "High price", "Low price", "Close price", "Volume", "Close time", "Quote Volume", 
           "Trades", "Taker buy base", "Taker buy quote"]

class CandleService:
    def __init__(self, coin, interval, start_time, end_time):
        self.coin = coin
        self.interval = interval
        self.start_time = start_time
        self.end_time = end_time


    def fetch_candle_info(self):
        url = "https://api.binance.com/api/v3/klines"

        headers = {
            "Content-Type": "application/json"
        }
        start_time = int(datetime.strptime(self.start_time, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
        end_time = int(datetime.strptime(self.end_time, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
        params = {
            "symbol": self.coin, "interval": self.interval, "startTime": start_time, "endTime": end_time
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        
            data = response.json()
            return data
        except Exception as e:
            print(e)


    def display_candle_info(self, data):
            if data == None:
                return

            cleaned_data = [row[:-1] for row in data]
            displayed_data = pandas.DataFrame(cleaned_data, columns=COLUMNS)
            displayed_data["Open time"] = pandas.to_datetime(displayed_data["Open time"], unit='ms')
            displayed_data["Close time"] = pandas.to_datetime(displayed_data["Close time"], unit='ms')
            return displayed_data


