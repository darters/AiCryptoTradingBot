import requests
from datetime import datetime
from binance.client import Client

class BinanceService:
    def __init__(self, testnet_api, secret_api):
        self.client = Client(testnet_api, secret_api, testnet=True)

    def createOrders(self, symbol, entry_price, take_profit, stop_loss, quantity):
        order = self.client.futures_create_order(
            symbol=symbol,
            side="BUY",
            type="LIMIT",
            quantity=quantity,
            price=entry_price,
            timeInForce="GTC"
        )
        tp_order = self.client.futures_create_order(
            symbol=symbol,
            side="SELL",
            type="TAKE_PROFIT_MARKET",
            stopPrice=take_profit,
            quantity=quantity,
            reduceOnly=True
        )
        sl_order = self.client.futures_create_order(
            symbol=symbol,
            side="SELL",
            type="STOP_MARKET",
            stopPrice=stop_loss,
            quantity=quantity,
            reduceOnly=True
        )
        return order, tp_order, sl_order

    def get_balance(self):
        balance = self.client.futures_account_balance()
        usdt_balance = float(next((item['balance'] for item in balance if item['asset'] == 'USDT')))
        print(f"Your balance: ${round(usdt_balance, 2)}")
    
    def fetch_candle_info(self, symbol, interval, start_time, end_time):
        url = "https://testnet.binancefuture.com/fapi/v1/"
        start_time = int(datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
        end_time = int(datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
        params = {
            "symbol": symbol, "interval": interval, "startTime": start_time, "endTime": end_time
        }
        try:
            candles_url = f"{url}klines"
            response = requests.get(candles_url, params=params)
            response.raise_for_status()
            data = response.json()
            last_data = None
            if interval not in ['1m', '3m']:
                current_candle_url = f"{url}ticker/price"
                current_candle_response = requests.get(current_candle_url, params = {"symbol": symbol})
                current_candle_response.raise_for_status()
                last_data = current_candle_response.json()['price']
                print("Last price ", last_data)
            return data, last_data
        except Exception as e:
            print(f'📢 Error while sending request to BINANCE: {e}')

    # def fetch_candle_info(self, symbol, interval, start_time, end_time):
    #     url = "https://fapi.binance.com/fapi/v1/"
    #     start_time = int(datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
    #     end_time = int(datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
    #     params = {
    #         "symbol": symbol, "interval": interval, "startTime": start_time, "endTime": end_time
    #     }
    #     try:
    #         candles_url = f"{url}klines"
    #         response = requests.get(candles_url, params=params)
    #         response.raise_for_status()
    #         data = response.json()
    #         last_data = None
    #         if interval not in ['1m', '3m']:
    #             current_candle_url = f"{url}ticker/price"
    #             current_candle_response = requests.get(current_candle_url, params = {"symbol": symbol})
    #             current_candle_response.raise_for_status()
    #             last_data = current_candle_response.json()['price']
    #             print("Last price ", last_data)
    #         return data, last_data
    #     except Exception as e:
    #         print(f'📢 Error while sending request to BINANCE: {e}')

  
         

