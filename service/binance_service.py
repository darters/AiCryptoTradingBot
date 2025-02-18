from binance.client import Client

class BinanceService:
    def __init__(self, testnet_api, secret_api):
        self.client = Client(testnet_api, secret_api, testnet=True)


    def createOrder(self, symbol, take_profit, stop_loss, quantity, entry_price):

        order = self.client.futures_create_order(
            symbol=symbol,
            side="BUY",
            type="LIMIT",
            quantity=quantity,
            price=entry_price,
            timeInForce="GTC"
        )
        print("Order was created: ", order)
        tp_order = self.client.futures_create_order(
            symbol=symbol,
            side="SELL",
            type="LIMIT",
            quantity=quantity,
            price=take_profit,
            timeInForce="GTC"
        )
        print("Take profit is: ", tp_order)
        sl_order = self.client.futures_create_order(
            symbol=symbol,
            side="SELL",
            type="STOP_MARKET",
            stopPrice=stop_loss,
            closePosition=True
        )
        print("Stop profit is: ", sl_order)
    
    def getBalance(self):
        balance = self.client.futures_account_balance()
        usdt_balance = float(next((item['balance'] for item in balance if item['asset'] == 'USDT')))
        print(f"Your balance: ${round(usdt_balance, 2)}")
   


